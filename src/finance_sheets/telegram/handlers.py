# handlers.py - define os handlers de comandos e callbacks do bot

import json
from telegram import Update

from finance_sheets.telegram.ui.keyboards import root_keyboard
from finance_sheets.services.gemini import gemini_service
from finance_sheets.services.sheets import sheets_service

from finance_sheets.utils.dates import get_current_month_name

# função auxiliar para enviar respostas ao usuário
async def send_response(update: Update, text: str, keyboard=None):
    if update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text=text, reply_markup=keyboard, parse_mode="HTML")
    else:
        await update.message.reply_text(text=text, reply_markup=keyboard, parse_mode="HTML")


async def menu(update: Update):
    await send_response(update, "<b>Olá eu sou o bot do dinheiro 🤑</b>\nEscolha uma opção:", root_keyboard())


async def saldo(update: Update):
    user = update.effective_user
    current_month = get_current_month_name()
    text = f"\nEm <i>{current_month}</i> seu saldo é de <b>{sheets_service.get_month_balance()}</b>"

    await send_response(update, text, root_keyboard())


async def entradas(update: Update):
    current_month = get_current_month_name()
    text = f"\nEm <i>{current_month}</i> suas entradas somam <b>{sheets_service.get_month_income()}</b>"
    
    await send_response(update, text, root_keyboard())


async def saidas(update: Update):
    current_month = get_current_month_name()
    text = f"\nEm <i>{current_month}</b> suas saídas somam <i>{sheets_service.get_month_expense()}</i>"

    await send_response(update, text, root_keyboard())


async def handle_ai_response(update):
    user_name = update.effective_user.first_name
    date = update.message.date.strftime("%d/%m/%Y")
    message_text = update.message.text

    gemini_response = gemini_service.interpret_text(message_text, date)
    response = json.loads(gemini_response)

    if (response["type"] == "response"):
        await send_response(update, response["resposta"])

    elif (response["type"] == "transaction"):
        sheets_service.insert_transaction(response)
        await send_response(update, f"{response['tipo']} registrada na planilha, {user_name}!")
