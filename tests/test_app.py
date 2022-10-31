import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.app import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    assert app.title == "FastAPI"
    assert app.version == "0.1.0"
