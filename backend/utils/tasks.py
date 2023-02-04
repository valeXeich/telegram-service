import asyncio

from faker import Faker

from service.chats import get_chats

fake = Faker()


async def message_distribution(client, session):
    chats = await get_chats(session)
    if not chats:
        return
    counter = 0
    for chat_id in chats:
        await client.send_message(chat_id, fake.text())
        await asyncio.sleep(0.1)
        counter += 1
        if counter == 1000:
            break