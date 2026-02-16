# Epic Title: Develop a User-Friendly Dashboard

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Transaction(db.Model):
    __tablename__ = "transactions"
    
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account_id: int = db.Column(db.Integer, db.ForeignKey("accounts.id"), nullable=False)
    amount: float = db.Column(db.Float, nullable=False)
    transaction_type: str = db.Column(db.String(10), nullable=False)  # 'credit' or 'debit'
    description: str = db.Column(db.String(255), nullable=True)
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Transaction {self.id} - {self.transaction_type} - {self.amount}>"