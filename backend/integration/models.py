# Epic Title: Core Banking System Integration

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CoreBankingIntegration(db.Model):
    __tablename__ = "core_banking_integration_logs"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    request_details: str = db.Column(db.Text, nullable=False)
    response_details: str = db.Column(db.Text, nullable=True)
    status_code: int = db.Column(db.Integer, nullable=False)
    timestamp: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<CoreBankingIntegration {self.id} - {self.status_code} - {self.timestamp}>"