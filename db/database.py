from sqlalchemy.orm import declarative_base
import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

load_dotenv()

engine = create_async_engine(os.getenv("POSTGRES_DATABASE_URL"))
session_factory = async_sessionmaker(bind=engine)

Base = declarative_base()
