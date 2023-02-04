import secrets


async def generate_user_api_key():
    api_key = secrets.token_urlsafe(16)
    return api_key