from modules import Depends, Request, JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import JWTDecodeError
from typing import List
from pydantic import BaseModel
import os


class Setting(BaseModel):
    authjwt_secret_key: List[str] = "secret"
    authjwt_denylist_enabled: bool = True
    authjwt_denylist_token_checks: List[str] = ["access", "refresh"]


@AuthJWT.load_config
def get_config():
    return Setting()


AuthJWT.load_config(Setting)


def authentication_dependency(auth: AuthJWT = Depends()):
    try:
        auth.jwt_required()
        pass
    except JWTDecodeError:
        raise JSONResponse(status_code=401, content={"detail": "Not authenticated"})
