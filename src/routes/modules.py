from fastapi import Depends, Request, APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from config.utils_config import template
from config.auth_config import authentication_dependency
