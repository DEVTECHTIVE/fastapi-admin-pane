from fastapi import FastAPI, Depends, Request, Response, status
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from bcrypt import hashpw, gensalt, checkpw
from dotenv import load_dotenv
import os
import uvicorn
