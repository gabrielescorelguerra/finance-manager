from finance_sheets.services.sheets import SheetsService
from finance_sheets.services.user import get_user_sheet


class SheetsServiceFactory:
    def create(self, user):
        sheet_key = get_user_sheet(user)["sheet_key"]
        return SheetsService(sheet_key)

sheets_service_factory = SheetsServiceFactory()