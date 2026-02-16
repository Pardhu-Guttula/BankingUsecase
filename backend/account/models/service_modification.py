# Epic Title: Account Opening and Service Modifications

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ServiceModificationRequest(db.Model):
    __tablename__ = "service_modification_requests"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    account_id: int = db.Column(db.Integer, db.ForeignKey("accounts.id"), nullable=False)
    service_name: str = db.Column(db.String(100), nullable=False)
    new_value: str = db.Column(db.String(255), nullable=False)
    status: str = db.Column(db.String(20), default="Pending")
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<ServiceModificationRequest {self.id} for user {self.user_id}>"