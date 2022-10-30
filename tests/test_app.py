import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.app import app
from src.config.db_config import get_db
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    assert app.title == "FastAPI"
    assert app.version == "0.1.0"


def test_db():
    assert app.dependency_overrides.get(get_db) is not None
