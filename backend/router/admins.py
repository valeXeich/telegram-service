from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.api_key import APIKey
from sqlalchemy.ext.asyncio import AsyncSession

from auth.auth import get_admin_api_key
from db.db import get_session
from schemas.admins import APIkey
from service.apikeys import create_user_api_key
from service.apikeys import get_api_keys as api_keys
from settings import settings

router = APIRouter()


@router.get("/check-admin-code", status_code=status.HTTP_200_OK)
async def check_admin_api_key(api_key: str):
    if api_key == settings.admin_api_key:
        return {"api_key": api_key}
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Invalid API KEY")


@router.post("/create-api-key", status_code=status.HTTP_201_CREATED, response_model=APIkey)
async def create_api_key(
    session: AsyncSession = Depends(get_session),
    api_key: APIKey = Depends(get_admin_api_key)
):
    data = await create_user_api_key(session)
    return data


@router.get("/get-api-keys", status_code=status.HTTP_200_OK)
async def get_api_keys(
    session: AsyncSession = Depends(get_session),
    api_key: APIKey = Depends(get_admin_api_key)
):
    keys = await api_keys(session=session)
    return [{"api_key": key} for key in keys]
