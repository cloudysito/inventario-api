from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db
from models import Productos, Base
from pydantic import BaseModel

class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    categoria: str
    stock: int = 0

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/productos/")
def listar(db:  Session = Depends(get_db)):
    return db.query(Productos).all()

@app.get("/productos/{id}")
def obtener_productos_id(id: int, db: Session = Depends(get_db)):
    jf  = db.query(Productos).filter(Productos.id == id).first()
    if jf is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return jf
    
@app.post("/productos/")
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):    
    nuevo_producto = Productos(
        nombre=producto.nombre,
        precio=producto.precio,
        categoria=producto.categoria,
        stock=producto.stock
    )
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

@app.post("/productos/{id}/descuento/")
def aplicar_descuento(id: int, porcentaje: float, db: Session = Depends(get_db)):
    producto = db.query(Productos).filter(Productos.id == id).first()
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    producto.precio = producto.precio * (1 - porcentaje / 100)
    db.commit()
    db.refresh(producto)
    return producto 