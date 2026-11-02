# inventario-api

REST API for product inventory management, built with FastAPI, SQLAlchemy and a layered architecture (Repository → Service → Router).

## Features
- ✅ List all products
- ✅ Get product by ID
- ✅ Create a new product
- ✅ Update a product
- ✅ Delete a product
- ✅ Apply a percentage discount to a product

## Tests
Run the test suite with:

```bash
pytest
```

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
