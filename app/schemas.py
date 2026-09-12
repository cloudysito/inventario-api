from pydantic import BaseModel, ConfigDict


class ProductCreate(BaseModel):
    name: str
    price: float
    category: str
    stock: int = 0


class ProductUpdate(BaseModel):
    name: str | None = None
    price: float | None = None
    category: str | None = None
    stock: int | None = None


class ProductOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    price: float
    category: str
    stock: int
