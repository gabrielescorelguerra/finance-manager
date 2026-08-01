import gspread
from google.oauth2.service_account import Credentials
from finance_sheets.utils.dates import add_months
from finance_sheets.constants import SheetsColumns
from finance_sheets.services.user import get_user_sheet
from dotenv import load_dotenv
import os

load_dotenv()


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets"
]

class SheetsService:
    # abre a planilha
    def __init__(self, sheet_key=None):
        # se usar apenas uma planilha, não precisa passar o sheet_key, ele pega do .env
        if sheet_key is None:
            sheet_key = os.getenv("SHEET_KEY")

        creds = Credentials.from_service_account_file(
            "./service-account.json",
            scopes=SCOPES
        )
        self.client = gspread.authorize(creds)

        self.sheet = self.client.open_by_key(sheet_key)

        self.cash_flow_worksheet = self.sheet.worksheet("Fluxo")
        self.data_worksheet = self.sheet.worksheet("Dados")


    # retorna a linha a inserir os novos dados
    def get_fisrt_empty_row(self):
        return self.cash_flow_worksheet.acell("M1").value


    # adiciona linhas de parcelas à lista de linhas a serem inseridas na planilha
    def append_installments_rows(self, rows, parent_row, installment_amount, row_index):
        parent_row[SheetsColumns.GROUP_ID] = parent_row[SheetsColumns.ID]
        installment_row = parent_row.copy()

        installment_row[SheetsColumns.VALUE] = parent_row[SheetsColumns.INSTALLMENT_VALUE] #calor
        installment_row[SheetsColumns.INSTALLMENT_AMOUNT] = None # se der erro coloca ""
        installment_row[SheetsColumns.INSTALLMENT_VALUE] = None

        for i in range(installment_amount):
            installment_row[SheetsColumns.DESCRIPTION] = (f"{parent_row[SheetsColumns.DESCRIPTION]} ({i + 1}/{parent_row[SheetsColumns.INSTALLMENT_AMOUNT]})")
            installment_row[SheetsColumns.ID] = row_index + i + 1
            installment_row[SheetsColumns.DATE] = add_months(parent_row[SheetsColumns.DATE], i)

            rows.append(installment_row.copy())


    # insere as linhas da transação na planilha
    def insert_transaction(self, data):
        row_index = int(self.get_fisrt_empty_row())

        parent_row = [row_index,
                    "",
                    data["data"],
                    data["descricao"],
                    data["valor"],
                    data["tipo"],
                    data["categoria"],
                    data["conta"],
                    data["pago"],
                    data["metodo"],
                    data["quantidade_parcelas"],
                    data["valor_parcela"],
                ]

        rows = [parent_row]
        installment_amount = data["quantidade_parcelas"]

        extra_rows = 0
        if (installment_amount):
            self.append_installments_rows(rows, parent_row, installment_amount, row_index)
            extra_rows = installment_amount

        self.cash_flow_worksheet.update(
            range_name=f"A{row_index}:L{row_index + extra_rows}",
            values=rows
        )

    def get_month_balance(self):
        return self.data_worksheet.acell("X4").value

    def get_month_income(self):
        return self.data_worksheet.acell("X5").value

    def get_month_expense(self):
        return self.data_worksheet.acell("X6").value
