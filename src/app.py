from .__init__ import *


@app.get("/")
def root():
    return {"msg": "Hello World!"}
