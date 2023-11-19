from typing import Optional

from fastapi import HTTPException
from fastapi_jwt_auth import AuthJWT
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from werkzeug.security import check_password_hash, generate_password_hash

from app.models.base import User
from app.models.roles import Role
from app.schemas.users import RegisterForm


async def authorize_user(login: str, session: AsyncSession):
    query = select(User).where((getattr(User, "login") == login))
    return (await session.execute(query)).scalars().first()


def authenticate_user(form_password: str, user: Optional[User], Authorize: AuthJWT):
    if not user:
        raise HTTPException(status_code=404, detail="User doesn't exist")
    elif not check_password_hash(user.password, form_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return generate_token(user.id, Authorize)


def generate_token(user_id: int, Authorize: AuthJWT):
    access_token = Authorize.create_access_token(subject=user_id)
    return access_token


async def create_user(form: RegisterForm, session: AsyncSession):
    role = await get_default_role(session)
    user = User(
        name=form.name,
        surname=form.surname,
        patronymic=form.patronymic,
        faculty=form.faculty,
        course=form.course,
        group=form.group,
        email=form.email,
        telegram=form.telegram,
        login=form.login,
        password=generate_password_hash(form.password.get_secret_value()),
        is_active=True,
        role=role,
    )
    session.add(user)
    await session.commit()
    return user


async def get_default_role(session: AsyncSession):
    get_role = select(Role).where(Role.name == "Студент")
    role = await session.execute(get_role)
    return role.scalars().first()
