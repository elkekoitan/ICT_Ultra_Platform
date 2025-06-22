import sys, pathlib, pytest
from fastapi.testclient import TestClient

# tests klasörü altından çalışıldığında üst dizini import path'e ekle
ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from services.gateway.main import app, API_KEY

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_connect_unauthorized():
    r = client.post("/connect", json={})
    assert r.status_code == 401


def test_trade_unauthorized():
    r = client.post("/trade", json={})
    assert r.status_code == 401 