from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_products_returns_200():
    response = client.get("/products/")
    assert response.status_code == 200


def test_post_create_product_returns_correct_name():
    payload = {
        "name": "Pytest Product",
        "price": 99.9,
        "category": "Testing",
        "stock": 5,
    }

    response = client.post("/products/", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == payload["name"]


def test_get_nonexistent_product_returns_404():
    response = client.get("/products/999")
    assert response.status_code == 404
