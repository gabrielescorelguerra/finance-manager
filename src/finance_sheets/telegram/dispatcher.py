# dispatcher.py - gerencia a lógica de roteamento de atualizações do bot

from telegram import Update
from telegram.error import BadRequest

from finance_sheets.telegram.registry import COMMAND_ROUTER, CALLBACK_ROUTER
from finance_sheets.telegram.handlers import handle_ai_response
from finance_sheets.telegram.bot import bot

import logging
import traceback

async def delete(update: Update):
    # determina chat_id e message_id com base no tipo de update (mensagem ou callback query)
    if update.message:
        chat_id = str(update.message.chat.id)
        message_id = str(update.message.message_id)
    elif update.callback_query:
        chat_id = str(update.callback_query.message.chat.id)
        message_id = str(update.callback_query.message.message_id)
    else:
        raise NotImplementedError()

    # delete a mensagem do chat
    await bot.delete_message(chat_id=int(chat_id), message_id=int(message_id))


async def route_update(update: Update):
    # verifica se o update tem um usuário efetivo (effective_user). Se não houver, retorna sem fazer nada.
    user = update.effective_user
    if not user:
        return

    try:
        # se for callback query (interação com botão)
        if update.callback_query:
            data = update.callback_query.data
            handler = CALLBACK_ROUTER.get(data)
            if handler:
                await handler(update)
            return

        if update.message and update.message.text:
            text = update.message.text.strip()

            # se o texto começar com "/", é um comando
            if text.startswith("/"):
                command = text.split("@")[0].split(" ")[0]
                handler = COMMAND_ROUTER.get(command)
                # chama o comando e deleta a mensagem do usuário
                if handler:
                    await handler(update)
                    # await delete(update)
                else:
                    # await delete(update)
                    await update.message.reply_text("Invalid command. Use the menu.")
            else:
                await handle_ai_response(update)
    except BadRequest:
        logging.warning(f"Telegram bad request: {traceback.format_exc()}")