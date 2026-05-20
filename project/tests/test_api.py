from fastapi.testclient import TestClient
from src.service.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_predict_validation():
    r = client.post("/predict", json={"X1": 0.5})
    assert r.status_code == 422