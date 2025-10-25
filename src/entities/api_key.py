from sqlalchemy import Column, String

from src.database.base import Base

class ApiKey(Base):
    __tablename__ = "api_keys"
    __table_args__ = {"schema": "gridknot"}

    api_key = Column(String(63), primary_key=True)