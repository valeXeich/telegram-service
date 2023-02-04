from pydantic import BaseModel


class APIkey(BaseModel):
    api_key: str
