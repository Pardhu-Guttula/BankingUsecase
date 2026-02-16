# Epic Title: Real-time Status Updates and Notifications

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class RequestStatus(db.Model):
    __tablename__ = "request_statuses"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    request_id: int = db.Column(db.Integer, nullable=False)
    status: str = db.Column(db.String(50), nullable=False)
    updated_at: datetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<RequestStatus {self.id} - {self.request_id} - {self.status}>"

class Notification(db.Model):
    __tablename__ = "notifications"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    message: str = db.Column(db.String(255), nullable=False)
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)
    is_read: bool = db.Column(db.Boolean, default=False)

    def __repr__(self) -> str:
        return f"<Notification {self.id} - {self.user_id} - {self.message}>"