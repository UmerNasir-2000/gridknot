from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.database.base import Base
from src.database.connection import engine, get_db
from src.entities.api_key import ApiKey
from src.middlewares import register_middlewares

app = FastAPI()

Base.metadata.create_all(bind=engine)

register_middlewares(app)

@app.get("/")
def root():
    return {'message': 'Hello World'}

@app.get("/api-keys")
def root(db: Session = Depends(get_db)):
    rows = db.query(ApiKey).all()
    return rows
