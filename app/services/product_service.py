from sqlalchemy.orm import Session

from app.models import Product
from app.repositories.product_repository import ProductRepository
from app.schemas import ProductCreate


def list_products(db: Session) -> list[Product]:
    return ProductRepository(db).list_all()


def get_product(db: Session, id: int) -> Product | None:
    return ProductRepository(db).get_by_id(id)


def create_product(db: Session, product: ProductCreate) -> Product:
    return ProductRepository(db).create(
        name=product.name,
        price=product.price,
        category=product.category,
        stock=product.stock,
    )


def apply_discount(db: Session, id: int, percentage: float) -> Product | None:
    repo = ProductRepository(db)
    product = repo.get_by_id(id)
    if product is None:
        return None

    product.price = product.price * (1 - percentage / 100)
    return repo.save_changes(product)
