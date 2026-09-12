from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import ProductoCreate
from services import producto_service

router = APIRouter(prefix="/productos", tags=["productos"])


@router.get("/")
def listar(db: Session = Depends(get_db)):
    return producto_service.listar_productos(db)


@router.get("/{id}")
def obtener_productos_id(id: int, db: Session = Depends(get_db)):
    producto = producto_service.obtener_producto(db, id)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto


@router.post("/")
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    return producto_service.crear_producto(db, producto)


@router.post("/{id}/descuento/")
def aplicar_descuento(id: int, porcentaje: float, db: Session = Depends(get_db)):
    producto = producto_service.aplicar_descuento(db, id, porcentaje)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto
