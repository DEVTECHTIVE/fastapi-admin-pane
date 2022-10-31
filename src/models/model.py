from .modules import *


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_admin = Column(Boolean, default=False)
    is_staff = Column(Boolean, default=False)
    craeted_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
