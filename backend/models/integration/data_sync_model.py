# Epic Title: Core Banking System Integration

from sqlalchemy import Column, Integer, DateTime, String, Boolean
from datetime import datetime
from backend.app import db


class DataSyncStatus(db.Model):
    __tablename__ = 'data_sync_statuses'

    id = Column(Integer, primary_key=True)
    entity = Column(String, nullable=False)
    last_synced_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    status = Column(String, nullable=False)
    is_success = Column(Boolean, default=True)

    def __init__(self, entity: str, last_synced_at: DateTime = None, status: str = 'pending', is_success: bool = True):
        self.entity = entity
        self.last_synced_at = last_synced_at if last_synced_at else datetime.utcnow()
        self.status = status
        self.is_success = is_success


# File 2: Data Sync Repository in repositories/integration/data_sync_repository.py