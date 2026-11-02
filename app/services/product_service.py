from sqlalchemy.orm import Session

from app.models import Product
from app.repositories.product_repository import ProductRepository
from app.schemas import ProductCreate, ProductUpdate


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


def update_product(db: Session, id: int, product: ProductUpdate) -> Product | None:
    repo = ProductRepository(db)
    existing_product = repo.get_by_id(id)
    if existing_product is None:
        return None

    updates = product.model_dump(exclude_unset=True, exclude_none=True)
    for field, value in updates.items():
        setattr(existing_product, field, value)

    return repo.save_changes(existing_product)


def delete_product(db: Session, id: int) -> bool:
    repo = ProductRepository(db)
    product = repo.get_by_id(id)
    if product is None:
        return False

    repo.delete(product)
    return True


def apply_discount(db: Session, id: int, percentage: float) -> Product | None:
    repo = ProductRepository(db)
    product = repo.get_by_id(id)
    if product is None:
        return None

    product.price = product.price * (1 - percentage / 100)
    return repo.save_changes(product)
