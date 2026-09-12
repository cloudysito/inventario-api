from sqlalchemy.orm import Session

from app.models import Productos
from app.schemas import ProductoCreate
from repositories import producto_repository


def listar_productos(db: Session) -> list[Productos]:
    return producto_repository.listar(db)


def obtener_producto(db: Session, id: int) -> Productos | None:
    return producto_repository.obtener_por_id(db, id)


def crear_producto(db: Session, producto: ProductoCreate) -> Productos:
    return producto_repository.crear(
        db,
        nombre=producto.nombre,
        precio=producto.precio,
        categoria=producto.categoria,
        stock=producto.stock,
    )


def aplicar_descuento(db: Session, id: int, porcentaje: float) -> Productos | None:
    producto = producto_repository.obtener_por_id(db, id)
    if producto is None:
        return None

    producto.precio = producto.precio * (1 - porcentaje / 100)
    return producto_repository.guardar_cambios(db, producto)
