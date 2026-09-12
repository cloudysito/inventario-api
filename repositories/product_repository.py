from sqlalchemy.orm import Session

from app.models import Product


def list_all(db: Session) -> list[Product]:
    return db.query(Product).all()


def get_by_id(db: Session, id: int) -> Product | None:
    return db.query(Product).filter(Product.id == id).first()


def create(db: Session, name: str, price: float, category: str, stock: int) -> Product:
    new_product = Product(
        name=name,
        price=price,
        category=category,
        stock=stock,
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


def save_changes(db: Session, product: Product) -> Product:
    db.commit()
    db.refresh(product)
    return product
