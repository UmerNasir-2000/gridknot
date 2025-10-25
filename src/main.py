from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.database.base import Base
from src.database.connection import engine, get_db
from src.middlewares import register_middlewares

app = FastAPI()

Base.metadata.create_all(bind=engine)

register_middlewares(app)

@app.get("/")
def root(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT NOW()"))
    time_now = result.scalar()
    return {"message": f"Hello World at {time_now}"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
