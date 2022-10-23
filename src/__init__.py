from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from bcrypt import hashpw, gensalt, checkpw
from dotenv import load_dotenv
import pathlib
import os
import uvicorn

PUBLIC_DIR = pathlib.Path("public").absolute()
TEMPLATE_DIR = pathlib.Path(PUBLIC_DIR).absolute().joinpath("templates")

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)

app.mount("/public", StaticFiles(directory="public"), name="public")


template = Jinja2Templates(directory=TEMPLATE_DIR)
