from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from telethon.errors import PhoneCodeExpiredError

from auth.auth import get_user_api_key
from db.db import get_session
from telegram_client import client
from utils.tasks import message_distribution

router = APIRouter()


@router.post("/login-telegram", status_code=status.HTTP_200_OK)
async def login_telegram(
    phone_number: str, phone_code: str | None = None, api_key=Depends(get_user_api_key)
):
    await client.connect()
    if not phone_code:
        await client.send_code_request(phone_number)
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            "To login you need a phone code, we sent it to you",
        )
    else:
        try:
            await client.sign_in(phone_number, phone_code)
        except PhoneCodeExpiredError:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, "Phone code expired")
    return {"ok": "Successfully login"}


@router.post("/send-messages")
async def send_messages(
    background_tasks: BackgroundTasks,
    session: AsyncSession = Depends(get_session),
    api_key=Depends(get_user_api_key),
):
    await client.connect()
    is_auth = await client.is_user_authorized()
    if is_auth:
        background_tasks.add_task(message_distribution, client, session)
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "You must log in to telegram")
    return {"ok": "Messaging started"}
