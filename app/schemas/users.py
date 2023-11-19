import re
from typing import Optional

from fastapi import HTTPException
from pydantic import BaseModel, SecretStr, constr, validator

from app.models.users import Faculties, User
from app.schemas import roles


class RegisterForm(BaseModel):
    name: constr(strip_whitespace=True, min_length=2, max_length=100)
    surname: constr(strip_whitespace=True, min_length=2, max_length=100)
    patronymic: Optional[constr(strip_whitespace=True, min_length=2, max_length=100)]

    faculty: Optional[Faculties]
    course: Optional[int]
    group: Optional[str]
    email: Optional[str]
    telegram: Optional[str]
    login: constr(strip_whitespace=True, min_length=2, max_length=100)
    password: SecretStr

    @validator("telegram")
    def telagram_val(cls, value):
        if value is not None:
            telegram_pattern = re.compile(r"^[a-z0-9_]{5,}$")
            if not re.match(telegram_pattern, value):
                raise HTTPException(
                    status_code=422,
                    detail="This telegram username format is not supported",
                )
            return value

    @validator("email")
    def email_val(cls, value):
        if value is not None:
            email_pattern = re.compile(r"^[\w.-]+@([\w-]+\.)+[\w-]{2,4}$")
            if not re.match(email_pattern, value):
                raise HTTPException(
                    status_code=422, detail="This email format is not supported"
                )
            return value

    # password must contain at least eight characters,
    # at least one number and both lower and uppercase letters and special characters
    @validator("password")
    def password_val(cls, value: SecretStr):
        password_pattern = re.compile(
            r"^(?=.*[a-zа-я])(?=.*[A-ZА-Я])(?=.*\d)(?=.*[@$!_%*?&])[A-Za-zа-яА-Я\d@$!_%*?&]{8,}$"
        )
        min_length = 8
        if len(value.get_secret_value()) < min_length:
            raise HTTPException(
                status_code=422, detail="This password format is not supported"
            )
        if not re.match(password_pattern, value.get_secret_value()):
            raise HTTPException(
                status_code=422, detail="This password format is not supported"
            )
        return value


class JSONForm(BaseModel):
    id: int
    name: str
    surname: str
    patronymic: str
    faculty: Faculties
    course: int
    group: str
    email: str
    telegram: str
    login: str
    is_active: bool
    role: roles.JSONForm

    @classmethod
    def custom_init(cls, user: User):
        return cls(
            id=user.id,
            name=user.name,
            surname=user.surname,
            patronymic=user.patronymic,
            faculty=user.faculty,
            course=user.course,
            group=user.group,
            email=user.email,
            telegram=user.telegram,
            login=user.login,
            is_active=user.is_active,
            role=roles.JSONForm.custom_init(user.role),
        )


class LogInForm(BaseModel):
    login: str
    password: SecretStr
