from .modules import *

router = APIRouter(tags=["user"], prefix="/user", responses={404: {"description": "Not found"}})


@router.get("/login")
def login(request: Request):
    return template.TemplateResponse("login.html", {"request": request})


@router.post("/{username}")
def get_user_by_username(username: str):
    return {"username": username}
