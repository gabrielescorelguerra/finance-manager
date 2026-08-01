# startup.py - inicializa o bot e configura o webhook

from finance_sheets.telegram.bot import bot    
from telegram import BotCommand
import logging

async def configure_bot(webhook_url: str):
    logging.info(f"Configuring bot webhook at URL: {webhook_url}")
    commands = [
        BotCommand("start", "Start the bot"),
        BotCommand("menu", "Menu"),
        BotCommand("saldo", "Saldo"),
        BotCommand("entradas", "Entradas"),
        BotCommand("saidas", "Saídas")
    ]
    await bot.set_my_commands(commands)
    await bot.set_webhook(webhook_url)
    