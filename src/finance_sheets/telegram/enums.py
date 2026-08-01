# enums.py - define os enums usados no bot

from enum import Enum

class CallbackData(Enum):
    MENU = "menu"
    SALDO = "saldo"
    ENTRADAS = "entradas"
    SAIDAS = "saidas"
