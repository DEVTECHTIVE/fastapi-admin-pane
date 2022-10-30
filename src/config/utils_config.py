from fastapi.templating import Jinja2Templates
import pathlib


PUBLIC_DIR = pathlib.Path("public").absolute()
TEMPLATE_DIR = pathlib.Path(PUBLIC_DIR).absolute().joinpath("templates")

template = Jinja2Templates(directory=TEMPLATE_DIR)
