from fastapi import FastAPI

from app.database import Base, engine
from routers import productos

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(productos.router)
