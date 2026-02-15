# Epic Title: Core Banking System Integration

from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from backend.app import core_banking_db as db

class CoreBankingIntegration(db.Model):
    __bind_key__ = 'core_banking'
    __tablename__ = 'core_banking_integrations'

    id = Column(Integer, primary_key=True)
    service_name = Column(String(50), nullable=False)
    endpoint = Column(String(255), nullable=False)
    request_type = Column(String(10), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, service_name: str, endpoint: str, request_type: str):
        self.service_name = service_name
        self.endpoint = endpoint
        self.request_type = request_type