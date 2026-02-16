# Epic Title: Personalized Dashboard

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Account(db.Model):
    __tablename__ = "accounts"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    account_number: str = db.Column(db.String(20), unique=True, nullable=False)
    account_type: str = db.Column(db.String(50), nullable=False)
    balance: float = db.Column(db.Float, nullable=False, default=0.0)
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Account {self.account_number}>"

class Transaction(db.Model):
    __tablename__ = "transactions"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account_id: int = db.Column(db.Integer, db.ForeignKey("accounts.id"), nullable=False)
    amount: float = db.Column(db.Float, nullable=False)
    transaction_type: str = db.Column(db.String(50), nullable=False)
    timestamp: datetime = db.Column(db.DateTime, default=datetime.utcnow)
    description: str = db.Column(db.String(255), nullable=True)

    def __repr__(self) -> str:
        return f"<Transaction {self.amount} {self.transaction_type}>"

class Widget(db.Model):
    __tablename__ = "widgets"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    name: str = db.Column(db.String(50), nullable=False)
    config: str = db.Column(db.Text, nullable=True)  # JSON or any serialized config
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Widget {self.name}>"