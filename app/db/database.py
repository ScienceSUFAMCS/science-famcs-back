from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.getenv("POSTGRES_DATABASE_URL"))
SessionLocal = sessionmaker(autocommit=False, bind=engine)

Base = declarative_base()
