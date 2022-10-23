from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from fastapi_jwt_auth.auth_jwt import AuthJWT
from pydantic import BaseModel
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


class Setting(BaseModel):
    authjwt_secret_key: str = os.getenv("SECRET_KEY")
    authjwt_denylist_enabled: bool = True
    authjwt_denylist_token_checks: List[str] = ["access", "refresh"]
    authjwt_token_location: List[str] = ["cookies"]


@AuthJWT.load_config
def get_config():
    return Setting()
