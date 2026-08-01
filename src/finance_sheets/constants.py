# constants.py - define constantes usadas no projeto

from enum import IntEnum

class SheetsColumns(IntEnum):
    ID = 0
    GROUP_ID = 1
    DATE = 2
    DESCRIPTION = 3
    VALUE = 4
    TYPE = 5
    CATEGORY = 6
    ACCOUNT = 7
    IS_PAID = 8
    METHOD = 9
    INSTALLMENT_AMOUNT = 10
    INSTALLMENT_VALUE = 11

