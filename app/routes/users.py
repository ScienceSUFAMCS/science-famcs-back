from fastapi import APIRouter, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.responses import JSONResponse

from app.controllers.auth import authenticate_user, authorize_user, create_user
from app.routes.middlewares import get_session
from app.schemas import users
from app.schemas.users import LogInForm, RegisterForm

user_router = APIRouter(prefix="/users")


@user_router.post("/login")
async def login(
    data: LogInForm,
    Authorize: AuthJWT = Depends(),
    session: AsyncSession = Depends(get_session),
):
    user = await authorize_user(data.login, session)
    access_token = authenticate_user(data.password.get_secret_value(), user, Authorize)
    response = JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "data": {"access_token": access_token},
            "message": "Successfully logged in",
        },
    )
    return response


@user_router.post("/register")
async def register(
    data: RegisterForm,
    Authorize: AuthJWT = Depends(),
    session: AsyncSession = Depends(get_session),
):
    try:
        user = await create_user(data, session)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="User already exists")
    access_token = authenticate_user(data.password.get_secret_value(), user, Authorize)
    response = JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "data": {
                "access_token": access_token,
                "user": users.JSONForm.custom_init(user).dict(),
            },
            "message": "Successfully registered",
        },
    )
    return response
