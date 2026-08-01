from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from telegram import Update

from finance_sheets.telegram.bot import bot
from finance_sheets.telegram.dispatcher import route_update

import logging

router = APIRouter()

@router.post("/webhook")
async def respond(request: Request):
    try:
        data = await request.json()
        update = Update.de_json(data, bot)
        await route_update(update)
    except Exception as e:
        logging.error(f"Webhook update error: {e}", exc_info=True)
    return JSONResponse(
        content={
            "status": "ok"
        }
    )