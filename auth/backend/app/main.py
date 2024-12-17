from fastapi import FastAPI
from . import models, crud, schemas
from .database import engine
from .routers import product, user, order

# Create the database tables
models.Base.metadata.create_all(bind=engine)

def create_app() -> FastAPI:
    """
    Initializes and returns the FastAPI application.
    """
    app = FastAPI()
    _include_routes(app)
    return app

def _include_routes(app: FastAPI):
    """
    Includes all the API routes in the FastAPI application.
    """
    app.include_router(product.router, prefix="/products", tags=["products"])
    app.include_router(user.router, prefix="/users", tags=["users"])
    app.include_router(order.router, prefix="/orders", tags=["orders"])

# Initialize the FastAPI app
app = create_app()
