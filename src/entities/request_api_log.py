from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, CheckConstraint, func, text
from sqlalchemy.orm import relationship

from src.database.base import Base


class RequestApiLog(Base):
    __tablename__ = "request_api_logs"
    __table_args__ = (
        {"schema": "gridknot"},
        CheckConstraint("status IN ('BLOCKED', 'PROCESSED')", name="status_check"),
    )

    request_api_log_id = Column(Integer, primary_key=True)
    api_key = Column(String(63), ForeignKey("gridknot.api_keys.api_key"), nullable=False)
    status = Column(String(15), nullable=False)
    expires_on = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("NOW() + INTERVAL '1 hour'")
    )
    created_at = Column(
        TIMESTAMP,
        nullable=False,
        server_default=func.now()
    )

    # Optional: relationship back to ApiKey
    api_key_ref = relationship("ApiKey", backref="request_logs")
