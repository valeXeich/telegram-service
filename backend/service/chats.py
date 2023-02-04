from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import Chat

async def get_chats(session: AsyncSession):
    query = select(Chat.chat_id).select_from(Chat)
    result = await session.execute(query)
    return result.scalars().all()