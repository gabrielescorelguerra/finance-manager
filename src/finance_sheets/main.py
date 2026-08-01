# main.py - define a aplicação FastAPI e configura o bot do Telegram

import logging
from contextlib import asynccontextmanager
import os

from fastapi import FastAPI

from finance_sheets.telegram.startup import configure_bot
from finance_sheets.routes.webhook import router as webhook_router

# vai imprimir
logging.getLogger().setLevel(logging.INFO)

ENV = os.getenv("ENVIRONMENT", "production")  # "local" ou "production"
PORT = 8000

@asynccontextmanager
async def lifespan(app: FastAPI):
    if ENV == "local": 
        from pyngrok import ngrok
        http_tunnel = ngrok.connect(PORT, bind_tls=True)
        webhook_url = f"{http_tunnel.public_url}/webhook"
    else:
        webhook_url = os.getenv("WEBHOOK_URL")

    await configure_bot(webhook_url)
    yield


app = FastAPI(
    description="Telegram bot",
    version="0.0.1",
    lifespan=lifespan
)

app.include_router(webhook_router)
