from fastapi import FastAPI

from .rate_limit_middleware import rate_limiting_middleware

def register_middlewares(app: FastAPI):
    app.middleware("http")(rate_limiting_middleware)