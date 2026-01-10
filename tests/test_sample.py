from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# CAMBIAR METODOS
# Test for POST /figuras busca la figura en concreto una figura de Anime
def test_process_data():
    response = client.post("/figuras", json={"nombre": "Goku Super Saiyan Blue", "precio": 55.00, "stock":12, "categoria":"Anime"})
    assert response.status_code == 200
    assert response.json() == {"result": 15}


# Test for POST /figuras with invalid data
def test_process_data_invalid():
    response = client.post("/figuras", json={"categoria": "Anime"})
    assert response.status_code == 422

# Test for GET /store (Devuelve todas)
def test_concatenate():
    response = client.get("/store?param1=Hello&param2=World")
    assert response.status_code == 200
    assert response.json() == {"result": "HelloWorld"}


