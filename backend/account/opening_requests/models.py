# Epic Title: Streamline Account Opening Requests

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AccountOpeningRequest(db.Model):
    __tablename__ = "account_opening_requests"
    
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    account_type: str = db.Column(db.String(20), nullable=False)
    initial_deposit: float = db.Column(db.Float, nullable=False)
    status: str = db.Column(db.String(20), default='pending')  # 'pending', 'approved', 'rejected'
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<AccountOpeningRequest {self.id} - {self.account_type} - {self.status}>"