# Epic Title: Account Opening and Service Modifications

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ApprovalRequest(db.Model):
    __tablename__ = "approval_requests"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    request_type: str = db.Column(db.String(50), nullable=False)  # E.g., 'AccountOpening', 'ServiceModification'
    request_id: int = db.Column(db.Integer, nullable=False)  # The ID of the related request
    status: str = db.Column(db.String(20), default="Pending")
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<ApprovalRequest {self.id} for {self.request_type} id={self.request_id}>"