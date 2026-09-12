from sqlalchemy.orm import Session

from app.models import Productos


def listar(db: Session) -> list[Productos]:
    return db.query(Productos).all()


def obtener_por_id(db: Session, id: int) -> Productos | None:
    return db.query(Productos).filter(Productos.id == id).first()


def crear(db: Session, nombre: str, precio: float, categoria: str, stock: int) -> Productos:
    nuevo_producto = Productos(
        nombre=nombre,
        precio=precio,
        categoria=categoria,
        stock=stock,
    )
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto


def guardar_cambios(db: Session, producto: Productos) -> Productos:
    db.commit()
    db.refresh(producto)
    return producto
