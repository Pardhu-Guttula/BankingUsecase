# Epic Title: Real-time Status Updates

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class RequestStatus(db.Model):
    __tablename__ = "request_statuses"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    request_id: int = db.Column(db.Integer, nullable=False)  # Link to user request
    status: str = db.Column(db.String(20), nullable=False)
    updated_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<RequestStatus {self.id} for request {self.request_id}>"