from sqlalchemy import Column, Integer, String

from .db import Base


class APIKeys(Base):
    __tablename__ = "apikeys"

    id = Column(Integer, primary_key=True)
    api_key = Column(String, unique=True, nullable=False)


class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True)
    chat_id = Column(String, unique=True, nullable=False)

