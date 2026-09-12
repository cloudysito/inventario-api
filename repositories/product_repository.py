from sqlalchemy.orm import Session

from app.models import Product

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def list_all(self) -> list[Product]:
        return self.db.query(Product).all()

    def get_by_id(self, id: int) -> Product | None:
        return self.db.query(Product).filter(Product.id == id).first()

    def create(self, name: str, price: float, category: str, stock: int) -> Product:
        new_product = Product(
            name=name,
            price=price,
            category=category,
            stock=stock,
        )
        self.db.add(new_product)
        self.db.commit()
        self.db.refresh(new_product)
        return new_product

    def save_changes(self, product: Product) -> Product:
        self.db.commit()
        self.db.refresh(product)
        return product

    def delete(self, product: Product) -> None:
        self.db.delete(product)
        self.db.commit()
