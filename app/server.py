from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from auth.router import router as auth_router
from db.connection import init_db


def make_middleware() -> list[Middleware]:
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

from fastapi import FastAPI

def create_app():
    app = FastAPI()
    
    # Middleware setup
    @app.middleware("http")
    async def add_process_time_header(request, call_next):
        response = await call_next(request)
        response.headers['X-Process-Time'] = str(process_time)
        return response

    # Include your routes here
    # app.include_router(your_router)

    return app

app = create_app()

def init_routers(app_: FastAPI) -> None:
    app_.include_router(auth_router)

