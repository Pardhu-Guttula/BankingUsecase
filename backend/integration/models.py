# Epic Title: Core Banking System Integration

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CoreBankingDataSync(db.Model):
    __tablename__ = "core_banking_data_sync"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    entity: str = db.Column(db.String(50), nullable=False)
    last_synced_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<CoreBankingDataSync {self.entity} - {self.last_synced_at}>"