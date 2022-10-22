from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from fastapi_jwt_auth.config import AuthJWTSettings
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


class Settings(AuthJWTSettings):
    authjwt_secret_key = os.getenv("SECRET_KEY")
    authjwt_denylist_enabled = True
    authjwt_denylist_token_checks = ["access", "refresh"]
    authjwt_token_location = ["cookies"]
