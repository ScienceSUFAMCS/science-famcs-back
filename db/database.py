import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

load_dotenv()

engine = create_async_engine(os.getenv("POSTGRES_DATABASE_URL"), echo=True)
session_factory = async_sessionmaker(bind=engine)

Base = declarative_base()
