import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router import admins, users
from utils.db import init_models


app = FastAPI(title='TelegramUserBot')
app.include_router(admins.router, tags=['Admin'])
app.include_router(users.router, tags=['User'])


origins = ["http://localhost:8080", "http://192.168.31.103:8080", "http://b126-188-163-102-106.ngrok.io", 'https://b126-188-163-102-106.ngrok.io']

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.on_event('startup')
# async def startup():
#     await init_models()


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT')))
