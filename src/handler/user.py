from .modules import *


def create_new_user(user: UserCreateSchema, db: Session):
    db = Users(username=user.username, email=user.email, password=user.password)
    db.commit()
    return user
