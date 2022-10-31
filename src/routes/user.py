from .modules import *

router = APIRouter(tags=["user"], prefix="/user", responses={404: {"description": "Not found"}})

user = {
    "username": "admin",
    "password": "admin",
}


@router.get("/login")
def login(request: Request):
    return template.TemplateResponse("login.html", {"request": request})


@router.get("/{username}")
def get_user_by_username(username: str):
    if user["username"] == username:
        return user
    return JSONResponse(status_code=404, content={"message": "User not found"})
