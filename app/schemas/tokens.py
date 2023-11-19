import os

from dotenv import load_dotenv
from fastapi_jwt_auth import AuthJWT
from pydantic.main import BaseModel

load_dotenv()


class Settings(BaseModel):
    authjwt_secret_key: str = os.getenv("SECRET")


@AuthJWT.load_config
def get_config():
    return Settings()
