from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 404

def test_process_data():
    response = client.post("/process", json={"text": "Pikachu"})
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert "description" in data
    assert "abilities" in data
    assert "colors" in data
    assert "size" in data
    assert data["name"] == "Pikachu"

def test_invalid_input():
    response = client.post("/process", json={})
    assert response.status_code == 422