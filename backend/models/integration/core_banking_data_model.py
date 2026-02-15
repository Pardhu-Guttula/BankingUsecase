# Epic Title: Core Banking System Integration

from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from backend.app import db


class CoreBankingData(db.Model):
    __tablename__ = 'core_banking_data'

    id = Column(Integer, primary_key=True)
    entity_id = Column(Integer, nullable=False)
    entity_type = Column(String, nullable=False)
    data = Column(String, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, entity_id: int, entity_type: str, data: str, updated_at: DateTime = None):
        self.entity_id = entity_id
        self.entity_type = entity_type
        self.data = data
        if updated_at is None:
            updated_at = datetime.utcnow()
        self.updated_at = updated_at


# File 2: Core Banking Data Repository in repositories/integration/core_banking_data_repository.py