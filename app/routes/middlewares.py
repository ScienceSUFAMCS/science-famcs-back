from fastapi import Depends
from fastapi.security import HTTPBearer
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import session_factory

auth_scheme = HTTPBearer(scheme_name="auth_scheme")


async def get_session() -> AsyncSession:
    async with session_factory() as session:
        yield session


def get_validated_token(token: str = Depends(auth_scheme), auth: AuthJWT = Depends()):
    auth.jwt_required(token=token)
    yield token
