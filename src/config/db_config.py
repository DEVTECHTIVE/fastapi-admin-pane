from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
import os

engines = create_engine(os.getenv("DATABASE_URL"))
Base = declarative_base()
local_session = sessionmaker(autocommit=False, autoflush=False, bind=engines)


def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()
