# registry.py - registra os handlers de comandos e callbacks do bot

from finance_sheets.telegram.enums import CallbackData
from finance_sheets.telegram.handlers import *

COMMAND_ROUTER = {
    "/start": menu,
    "/menu": menu,
    "/saldo": saldo,
    "/entradas": entradas,
    "/saidas": saidas,
}

CALLBACK_ROUTER = {
    CallbackData.MENU.value: menu,
    CallbackData.SALDO.value: saldo,
    CallbackData.ENTRADAS.value: entradas,
    CallbackData.SAIDAS.value: saidas,
}