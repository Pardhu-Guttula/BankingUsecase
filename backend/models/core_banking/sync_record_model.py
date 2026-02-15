# Epic Title: Core Banking System Integration

from sqlalchemy import Column, Integer, String, DateTime
from backend.app import db
import datetime

class SyncRecord(db.Model):
    __tablename__ = 'sync_records'

    id = Column(Integer, primary_key=True)
    entity = Column(String(50), nullable=False)
    last_sync_time = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    def __init__(self, entity: str, last_sync_time: datetime.datetime):
        self.entity = entity
        self.last_sync_time = last_sync_time


# File 2: Synchronization Repository to Handle CRUD Operations in integration/repositories/sync_record_repository.py