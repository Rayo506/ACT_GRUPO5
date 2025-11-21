from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# CAMBIAR METODOS
# Test for POST /figuras (guarda 1)
def test_process_data():
    response = client.post("/process", json={"value1": 10, "value2": 5})
    assert response.status_code == 200
    assert response.json() == {"result": 15}

# Test for POST /figuras with invalid data
def test_process_data_invalid():
    response = client.post("/process", json={"value1": 10})
    assert response.status_code == 422

# Test for GET /figuras (Devuelve todas)
def test_concatenate():
    response = client.get("/concat?param1=Hello&param2=World")
    assert response.status_code == 200
    assert response.json() == {"result": "HelloWorld"}


