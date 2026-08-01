# bot.py - inicializa o bot do Telegram e define os dados de callback

import os
from enum import Enum
from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = Bot(BOT_TOKEN)
