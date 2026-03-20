from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_productos_responde_200():
    response = client.get("/productos/")
    assert response.status_code == 200


def test_post_crear_producto_devuelve_nombre_correcto():
    payload = {
        "nombre": "Producto Pytest",
        "precio": 99.9,
        "categoria": "Testing",
        "stock": 5,
    }

    response = client.post("/productos/", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == payload["nombre"]


def test_get_producto_inexistente_responde_404():
    response = client.get("/productos/999")
    assert response.status_code == 404

