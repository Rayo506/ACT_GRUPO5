from fastapi.testclient import TestClient
from app.main import app
from app.crud import product_store

client = TestClient(app)


def setup_function():
    product_store.products = {}
    product_store.next_id = 1


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_create_product():
    product_data = {
        "product_name": "Dell XPS 15",
        "description": "High-performance laptop with 15-inch display",
        "unit_of_measure": "unit",
        "category": "laptop",
        "price": 1499.99,
        "brand": "Dell",
        "stock_quantity": 10,
        "specifications": {
            "processor": "Intel i7",
            "ram": "16GB",
            "storage": "512GB SSD"
        }
    }
    response = client.post("/products/", json=product_data)
    assert response.status_code == 201
    data = response.json()
    assert data["product_name"] == "Dell XPS 15"
    assert data["id"] == 1
    assert data["price"] == 1499.99


def test_read_products():
    product_data = {
        "product_name": "Logitech MX Master 3",
        "description": "Wireless mouse with advanced features",
        "unit_of_measure": "unit",
        "category": "mouse",
        "price": 99.99,
        "brand": "Logitech",
        "stock_quantity": 50
    }
    client.post("/products/", json=product_data)

    response = client.get("/products/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["product_name"] == "Logitech MX Master 3"


def test_read_product_by_id():
    product_data = {
        "product_name": "Samsung 27 Monitor",
        "description": "4K UHD monitor with HDR support",
        "unit_of_measure": "unit",
        "category": "monitor",
        "price": 399.99,
        "brand": "Samsung",
        "stock_quantity": 15
    }
    create_response = client.post("/products/", json=product_data)
    product_id = create_response.json()["id"]

    response = client.get(f"/products/{product_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["product_name"] == "Samsung 27 Monitor"
    assert data["id"] == product_id


def test_read_product_not_found():
    response = client.get("/products/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"


def test_update_product():
    product_data = {
        "product_name": "Kingston SSD",
        "description": "500GB SSD drive",
        "unit_of_measure": "unit",
        "category": "disk",
        "price": 79.99,
        "brand": "Kingston",
        "stock_quantity": 30
    }
    create_response = client.post("/products/", json=product_data)
    product_id = create_response.json()["id"]

    update_data = {
        "price": 69.99,
        "stock_quantity": 25
    }
    response = client.put(f"/products/{product_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["price"] == 69.99
    assert data["stock_quantity"] == 25
    assert data["product_name"] == "Kingston SSD"


def test_update_product_not_found():
    update_data = {
        "price": 99.99
    }
    response = client.put("/products/999", json=update_data)
    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"


def test_delete_product():
    product_data = {
        "product_name": "Mechanical Keyboard",
        "description": "RGB mechanical gaming keyboard",
        "unit_of_measure": "unit",
        "category": "keyboard",
        "price": 129.99,
        "brand": "Razer",
        "stock_quantity": 20
    }
    create_response = client.post("/products/", json=product_data)
    product_id = create_response.json()["id"]

    response = client.delete(f"/products/{product_id}")
    assert response.status_code == 204

    get_response = client.get(f"/products/{product_id}")
    assert get_response.status_code == 404


def test_delete_product_not_found():
    response = client.delete("/products/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"


def test_search_products_by_category():
    products = [
        {
            "product_name": "HP Laptop",
            "description": "Business laptop",
            "unit_of_measure": "unit",
            "category": "laptop",
            "price": 899.99,
            "brand": "HP",
            "stock_quantity": 5
        },
        {
            "product_name": "Lenovo Laptop",
            "description": "Gaming laptop",
            "unit_of_measure": "unit",
            "category": "laptop",
            "price": 1299.99,
            "brand": "Lenovo",
            "stock_quantity": 3
        },
        {
            "product_name": "Dell Monitor",
            "description": "24-inch monitor",
            "unit_of_measure": "unit",
            "category": "monitor",
            "price": 199.99,
            "brand": "Dell",
            "stock_quantity": 12
        }
    ]
    for product in products:
        client.post("/products/", json=product)

    response = client.get("/products/search/?category=laptop")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert all(p["category"] == "laptop" for p in data)


def test_search_products_by_brand():
    products = [
        {
            "product_name": "Dell XPS",
            "description": "Premium laptop",
            "unit_of_measure": "unit",
            "category": "laptop",
            "price": 1599.99,
            "brand": "Dell",
            "stock_quantity": 8
        },
        {
            "product_name": "Dell Monitor",
            "description": "27-inch monitor",
            "unit_of_measure": "unit",
            "category": "monitor",
            "price": 299.99,
            "brand": "Dell",
            "stock_quantity": 15
        }
    ]
    for product in products:
        client.post("/products/", json=product)

    response = client.get("/products/search/?brand=Dell")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert all(p["brand"] == "Dell" for p in data)


def test_pagination():
    for i in range(15):
        product_data = {
            "product_name": f"Product {i}",
            "description": f"Description {i}",
            "unit_of_measure": "unit",
            "category": "other",
            "price": 99.99,
            "brand": "Generic",
            "stock_quantity": 10
        }
        client.post("/products/", json=product_data)

    response = client.get("/products/?skip=5&limit=5")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 5
