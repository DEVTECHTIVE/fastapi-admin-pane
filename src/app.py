from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi_jwt_auth.exceptions import AuthJWTException
import uvicorn

from routes import admin, user

app = FastAPI()

app.mount("/public", StaticFiles(directory="public"), name="public")


@app.exception_handler(AuthJWTException)
def auth_jwt_exception_handler(request: Request, exc: AuthJWTException):
    return RedirectResponse(url="../user/login")


@app.get("/")
def root():
    return RedirectResponse(url="/admin")


app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)

app.include_router(admin.router)
app.include_router(user.router)


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True, workers=2)
