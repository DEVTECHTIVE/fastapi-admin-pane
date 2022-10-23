from __init__ import *


@app.get("/")
def root(request: Request):
    return template.TemplateResponse("base.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True, workers=2)
