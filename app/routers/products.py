from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import ProductCreate, ProductUpdate
from app.services import product_service

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


@router.patch("/{id}")
def update_product(id: int, product: ProductUpdate, db: DbSession):
    updated_product = product_service.update_product(db, id, product)
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id: int, db: DbSession):
    if not product_service.delete_product(db, id):
        raise HTTPException(status_code=404, detail="Product not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post("/{id}/discount/")
def apply_discount(id: int, percentage: float, db: DbSession):
    product = product_service.apply_discount(db, id, percentage)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
