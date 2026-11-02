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


def test_patch_product_updates_only_provided_fields():
    create_response = client.post(
        "/products/",
        json={
            "name": "Product to Update",
            "price": 20,
            "category": "Testing",
            "stock": 3,
        },
    )
    product_id = create_response.json()["id"]

    response = client.patch(
        f"/products/{product_id}",
        json={"price": 25},
    )

    assert response.status_code == 200
    data = response.json()
    assert data["price"] == 25
    assert data["name"] == "Product to Update"
    assert data["stock"] == 3


def test_patch_nonexistent_product_returns_404():
    response = client.patch("/products/999", json={"price": 25})
    assert response.status_code == 404


def test_delete_product_returns_204_and_removes_product():
    create_response = client.post(
        "/products/",
        json={
            "name": "Product to Delete",
            "price": 20,
            "category": "Testing",
            "stock": 3,
        },
    )
    product_id = create_response.json()["id"]

    delete_response = client.delete(f"/products/{product_id}")

    assert delete_response.status_code == 204
    assert client.get(f"/products/{product_id}").status_code == 404


def test_delete_nonexistent_product_returns_404():
    response = client.delete("/products/999")
    assert response.status_code == 404
