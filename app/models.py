from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Productos(Base):
    __tablename__ = "productos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String)
    precio: Mapped[float] = mapped_column(Float)
    categoria: Mapped[str] = mapped_column(String)
    stock: Mapped[int] = mapped_column(Integer, default=0)
