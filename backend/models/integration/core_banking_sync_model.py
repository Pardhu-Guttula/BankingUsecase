# Epic Title: Data Synchronization Mechanisms

from sqlalchemy import Column, Integer, String, DateTime
from backend.app import db
from datetime import datetime

class CoreBankingSync(db.Model):
    __tablename__ = 'core_banking_sync'

    id = Column(Integer, primary_key=True)
    entity = Column(String(255), nullable=False)
    last_synced = Column(DateTime, default=datetime.utcnow)

    def __init__(self, entity: str, last_synced: DateTime = None):
        self.entity = entity
        self.last_synced = last_synced or datetime.utcnow()


# File 2: Core Banking Data Sync Repository in `repositories/integration/core_banking_sync_repository.py`