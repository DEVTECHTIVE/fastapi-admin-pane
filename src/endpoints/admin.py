from .modules import *

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(authentication_dependency)],
)


@router.get("/", response_class=HTMLResponse)
def admin_home(request: Request):
    return template.TemplateResponse("base.html", {"request": request})
