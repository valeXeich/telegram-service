from telethon import TelegramClient

from settings import settings


client = TelegramClient('bot', settings.bot_api_id, settings.bot_api_hash)