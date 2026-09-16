# inventario-api

REST API for product inventory management, built with FastAPI, SQLAlchemy and a layered architecture (Repository → Service → Router).

## Features (working)
- ✅ List all products
- ✅ Get product by ID
- ✅ Create a new product
- ✅ Apply a percentage discount to a product

## In progress
- ⏳ Update product (schema ready, endpoint pending)
- ⏳ Delete product
- ⏳ Test coverage

## Tech Stack
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite (dev)

## Architecture
Layered structure: `routers/` (HTTP layer) → `services/` (business logic) → `repositories/` (data access) → SQLAlchemy models.

## Running locally
\`\`\`bash
pip install -r requirements.txt
uvicorn main:app --reload
\`\`\`
API docs available at `http://localhost:8000/docs` (FastAPI's automatic Swagger UI).
