import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Rate Limiter Example!"}

def test_fixed_limited_resource():
    response = client.get("/fixed-limited")
    assert response.status_code == 200
    assert response.json() == {"message": "You accessed the fixed-window limited resource!"}

def test_sliding_limited_resource():
    response = client.get("/sliding-limited")
    assert response.status_code == 200
    assert response.json() == {"message": "You accessed the sliding-window-log limited resource!"}

def test_fixed_limited_exceed_limit():
    for _ in range(5):
        client.get("/fixed-limited")
    response = client.get("/fixed-limited")
    assert response.status_code == 429  # Assuming 429 Too Many Requests is returned

def test_sliding_limited_exceed_limit():
    for _ in range(3):
        print(_)
        client.get("/sliding-limited")
    response = client.get("/sliding-limited")
    print(response.status_code)
    assert response.status_code == 429  # Assuming 429 Too Many Requests is returned