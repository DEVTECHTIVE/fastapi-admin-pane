from pydantic import BaseModel


class UserSchema(BaseModel):
    name: str
    email: str
    password: str
    is_staff: bool = False

    class Config:
        orm_mode = True


class UserAdminSchema(UserSchema):
    is_admin: bool = True

    class Config:
        orm_mode = True


class UserCreateSchema(UserSchema):
    pass


class UserUpdateSchema(UserSchema):
    pass


class UserDeleteSchema(BaseModel):
    id: int
