# registry.py - registra os handlers de comandos e callbacks do bot

from finance_sheets.telegram.enums import CallbackData
from finance_sheets.telegram.handlers import *

COMMAND_ROUTER = {
    "/start": menu,
    "/menu": menu,
    "/saldo": balance,
    "/entradas": income,
    "/saidas": expense,
}

CALLBACK_ROUTER = {
    CallbackData.MENU.value: menu,
    CallbackData.SALDO.value: balance,
    CallbackData.ENTRADAS.value: income,
    CallbackData.SAIDAS.value: expense,
}