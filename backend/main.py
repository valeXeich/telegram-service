import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router import admins, users
from utils.db import init_models


app = FastAPI(title='TelegramUserBot')
app.include_router(admins.router, tags=['Admin'])
app.include_router(users.router, tags=['User'])


origins = ["http://localhost:8080", "https://frontend-vue-production.up.railway.app"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event('startup')
async def startup():
    await init_models()


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT')))
