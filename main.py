from fastapi import FastAPI

from app.database import Base, engine
from app.routers import products

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(products.router)
