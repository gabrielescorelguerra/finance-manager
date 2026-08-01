# keyboards.py - define os teclados inline do bot

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from finance_sheets.telegram.enums import CallbackData

def root_keyboard():
    # callback data é o valor que será enviado de volta ao bot quando o botão for pressionado
    keyboard = [
        [
            InlineKeyboardButton("👤 Menu", callback_data=CallbackData.MENU.value),
            InlineKeyboardButton("💰 Saldo", callback_data=CallbackData.SALDO.value)
        ],
        [
            InlineKeyboardButton("📥 Entradas", callback_data=CallbackData.ENTRADAS.value),
            InlineKeyboardButton("📤 Saídas", callback_data=CallbackData.SAIDAS.value)
        ],
    ]
    return InlineKeyboardMarkup(keyboard)