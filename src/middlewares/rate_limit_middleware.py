from typing import Callable, Awaitable

from fastapi import Request, Response, HTTPException, status
from sqlalchemy.orm import Session

from src.database.connection import SessionLocal
from src.entities.api_key import ApiKey


async def rate_limiting_middleware(
        request: Request,
        call_next: Callable[[Request], Awaitable[Response]]) -> Response:
    db: Session = SessionLocal()
    try:
        api_key = request.headers.get("X-API-KEY", None)

        if api_key is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Missing X-API-KEY header"
            )

        api_key_from_db = db.get(ApiKey, api_key)

        if api_key_from_db is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid X-API-KEY header"
            )

        response = await call_next(request)
    finally:
        db.close()

    return response