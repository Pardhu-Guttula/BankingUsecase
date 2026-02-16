# Epic Title: Core Banking System Integration

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class LocalTransaction(db.Model):
    __tablename__ = "local_transactions"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    amount: float = db.Column(db.Float, nullable=False)
    transaction_type: str = db.Column(db.String(50), nullable=False)
    status: str = db.Column(db.String(50), nullable=False)
    timestamp: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<LocalTransaction {self.id} - {self.user_id} - {self.amount} - {self.transaction_type} - {self.status} - {self.timestamp}>"

class CoreBankingDataSync(db.Model):
    __tablename__ = "core_banking_data_sync"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    entity: str = db.Column(db.String(50), nullable=False)
    last_synced_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<CoreBankingDataSync {self.entity} - {self.last_synced_at}>"