from modules import create_engine, sessionmaker, declarative_base, os

engines = create_engine(os.getenv("DATABASE_URL"))
Base = declarative_base()
local_session = sessionmaker(autocommit=False, autoflush=False, bind=engines)


def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()
