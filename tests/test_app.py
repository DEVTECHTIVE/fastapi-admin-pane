import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.app import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_message():
    response = client.get("/test")
    assert response.status_code == 200
    assert response.json() == {"test": "test"}