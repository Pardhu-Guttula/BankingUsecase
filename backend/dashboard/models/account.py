# Epic Title: Develop a User-Friendly Dashboard

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Account(db.Model):
    __tablename__ = "accounts"
    
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    account_number: str = db.Column(db.String(20), unique=True, nullable=False)
    account_type: str = db.Column(db.String(20), nullable=False)
    balance: float = db.Column(db.Float, nullable=False, default=0.0)
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Account {self.account_number}>"