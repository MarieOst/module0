from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"message": "L'API est opérationnelle"}

def test_chat():
    response = client.post("/chat", json={"text": "Coucou"})
    assert response.status_code == 200
    assert response.json() == {"message": "Le message suivant a été reçu : Coucou."}
