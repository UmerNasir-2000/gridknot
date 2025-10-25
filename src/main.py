from fastapi import FastAPI

from src.middlewares import register_middlewares

app = FastAPI()

register_middlewares(app)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
