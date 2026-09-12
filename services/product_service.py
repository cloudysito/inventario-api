from sqlalchemy.orm import Session

from app.models import Product
from app.schemas import ProductCreate
from repositories import product_repository


def list_products(db: Session) -> list[Product]:
    return product_repository.list_all(db)


def get_product(db: Session, id: int) -> Product | None:
    return product_repository.get_by_id(db, id)


def create_product(db: Session, product: ProductCreate) -> Product:
    return product_repository.create(
        db,
        name=product.name,
        price=product.price,
        category=product.category,
        stock=product.stock,
    )


def apply_discount(db: Session, id: int, percentage: float) -> Product | None:
    product = product_repository.get_by_id(db, id)
    if product is None:
        return None

    product.price = product.price * (1 - percentage / 100)
    return product_repository.save_changes(db, product)
