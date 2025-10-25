from typing import Callable, Awaitable

from fastapi import Request, Response, Depends
from sqlalchemy.orm import Session

from src.database.connection import SessionLocal
from src.entities.api_key import ApiKey


async def rate_limiting_middleware(
        request: Request,
        call_next: Callable[[Request], Awaitable[Response]]) -> Response:
    db: Session = SessionLocal()
    try:
        rows = db.query(ApiKey).all()
        print(rows)
        response = await call_next(request)
    finally:
        db.close()

    return response