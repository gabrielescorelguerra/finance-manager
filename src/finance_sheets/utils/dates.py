# dates.py - define funções utilitárias para manipulação de datas

from datetime import datetime
from dateutil.relativedelta import relativedelta

def add_months (date_str, months):
    date = datetime.strptime(date_str, "%Y-%m-%d")

    return (date + relativedelta(months=months)).strftime("%Y-%m-%d")


def get_current_month_name():
    month_names = [
        "Janeiro", "Fevereiro", "Março",
        "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro",
        "Outubro", "Novembro", "Dezembro"
    ]

    return month_names[datetime.now().month - 1]