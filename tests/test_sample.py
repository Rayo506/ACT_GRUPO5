from fastapi.testclient import TestClient
from app.main import app
from app.crud import product_store

client = TestClient(app)

# Resetear antes de cada test
def setup_function():
    product_store.products = {}
    product_store.next_id = 1

# Test de root y health
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

# Crear figura
def test_create_figure():
    data = {
        "nombre": "Goku Super Saiyan Blue",
        "precio": 55.00,
        "stock": 12,
        "categoria": "Anime"
    }
    response = client.post("/figuras/", json=data)
    assert response.status_code == 200
    result = response.json()
    assert result["id"] == 1
    assert result["nombre"] == data["nombre"]
    assert result["precio"] == data["precio"]
    assert result["categoria"] == data["categoria"]

# Leer todas las figuras
def test_get_all_figures():
    # Primero creamos dos figuras
    client.post("/figuras/", json={"nombre": "Luffy Gear 5", "precio": 60, "stock": 8, "categoria": "Anime"})
    client.post("/figuras/", json={"nombre": "Batman Dark Knight", "precio": 75, "stock": 5, "categoria": "Comic"})

    response = client.get("/figuras/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    nombres = [f["nombre"] for f in data]
    assert "Luffy Gear 5" in nombres
    assert "Batman Dark Knight" in nombres

# Leer figura por ID
def test_get_figure_by_id():
    create = client.post("/figuras/", json={"nombre": "Naruto Sage Mode", "precio": 50, "stock": 10, "categoria": "Anime"})
    fid = create.json()["id"]

    response = client.get(f"/figuras/{fid}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == fid
    assert data["nombre"] == "Naruto Sage Mode"

# Leer figura por ID inexistente
def test_get_figure_not_found():
    response = client.get("/figuras/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Figura no encontrada"

# Actualizar figura
def test_update_figure():
    create = client.post("/figuras/", json={"nombre": "Sasuke Rinnegan", "precio": 65, "stock": 6, "categoria": "Anime"})
    fid = create.json()["id"]

    update = {"precio": 70, "stock": 8}
    response = client.put(f"/figuras/{fid}", json=update)
    assert response.status_code == 200
    data = response.json()
    assert data["precio"] == 70
    assert data["stock"] == 8
    assert data["nombre"] == "Sasuke Rinnegan"

# Actualizar figura no existente
def test_update_figure_not_found():
    response = client.put("/figuras/999", json={"precio": 100})
    assert response.status_code == 404
    assert response.json()["detail"] == "Figura no encontrada"

# Eliminar figura
def test_delete_figure():
    create = client.post("/figuras/", json={"nombre": "Vegeta Super Saiyan", "precio": 55, "stock": 9, "categoria": "Anime"})
    fid = create.json()["id"]

    response = client.delete(f"/figuras/{fid}")
    assert response.status_code == 200
    assert response.json()["message"] == "Figura eliminada"

    get_response = client.get(f"/figuras/{fid}")
    assert get_response.status_code == 404

# Eliminar figura no existente
def test_delete_figure_not_found():
    response = client.delete("/figuras/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Figura no encontrada"

# Buscar por categoría
def test_search_figures_by_category():
    client.post("/figuras/", json={"nombre": "Luffy Gear 5", "precio": 60, "stock": 8, "categoria": "Anime"})
    client.post("/figuras/", json={"nombre": "Batman Dark Knight", "precio": 75, "stock": 5, "categoria": "Comic"})
    client.post("/figuras/", json={"nombre": "Goku Ultra Instinct", "precio": 80, "stock": 3, "categoria": "Anime"})

    response = client.get("/figuras/search?category=Anime")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert all(f["categoria"] == "Anime" for f in data)
