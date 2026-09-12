from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import ProductCreate
from services import product_service

router = APIRouter(prefix="/products", tags=["products"])

DbSession = Annotated[Session, Depends(get_db)]


@router.get("/")
def list_products(db: DbSession):
    return product_service.list_products(db)


@router.get("/{id}")
def get_product_by_id(id: int, db: DbSession):
    product = product_service.get_product(db, id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/")
def create_product(product: ProductCreate, db: DbSession):
    return product_service.create_product(db, product)


@router.post("/{id}/discount/")
def apply_discount(id: int, percentage: float, db: DbSession):
    product = product_service.apply_discount(db, id, percentage)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
