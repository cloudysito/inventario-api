from sqlalchemy import Column, Integer, String, Float

from database import Base

class Productos(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    precio = Column(Float)
    categoria = Column(String)
    stock = Column(Integer, default=0)