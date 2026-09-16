from fastapi.testclient import TestClient
from app.api.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Industrial CV Inspection API running" in response.json()["message"]

def test_health():
    response = client.get("/health/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_premium_locked():
    response = client.get("/premium/video-inspection")
    assert response.status_code == 402

def test_inspect_image():
    import io
    from PIL import Image
    # Create a simple in-memory RGB image
    img = Image.new("RGB", (100, 100), color=(73, 109, 137))
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    response = client.post("/inspect/", files={"file": ("sample.png", buf, "image/png")})
    assert response.status_code == 200
    data = response.json()
    assert "detections" in data
    assert "metrics" in data
