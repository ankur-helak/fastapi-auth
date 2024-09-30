from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from auth.router import router as auth_router
from db.connection import init_db


def make_middleware() -> list[Middleware]:
    """Creates a list containing a CORS middleware instance.
    Parameters:
        None
    Returns:
        - list[Middleware]: A list with a single Middleware instance configured for CORS.
    Processing Logic:
        - The created middleware allows all origins, credentials, methods, and headers for cross-origin resource sharing."""
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    ]
    return middleware


def init_routers(app_: FastAPI) -> None:
    app_.include_router(auth_router)


def create_app() -> FastAPI:
    """Creates and returns a FastAPI application instance with pre-configured settings.
    Returns:
        - FastAPI: The FastAPI application instance with routes and middleware set up.
    Processing Logic:
        - The application title, description, version, and middleware are configured at initialization.
        - Routes are initialized through `init_routers`.
        - The database is initialized asynchronously on the startup event of the application."""
    app_ = FastAPI(
        title="Auth",
        description="Authentication APIs",
        version="1.0.0",
        middleware=make_middleware(),
    )
    init_routers(app_=app_)
    
    @app_.on_event("startup")
    async def startup_event():
        await init_db()
    return app_


app = create_app()