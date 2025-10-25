from typing import Callable, Awaitable

from fastapi import Request, Response

async def rate_limiting_middleware(
        request: Request,
        call_next: Callable[[Request], Awaitable[Response]]) -> Response:
    return await call_next(request)