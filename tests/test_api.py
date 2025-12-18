from fastapi.testclient import TestClient
from app.api.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_premium_locked():
    response = client.get("/premium/video-inspection")
    assert response.status_code == 402
