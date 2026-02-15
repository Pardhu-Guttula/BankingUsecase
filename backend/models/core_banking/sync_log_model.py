# Epic Title: Core Banking System Integration

from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from backend.app import db

class SyncLog(db.Model):
    __tablename__ = 'sync_logs'

    id = Column(Integer, primary_key=True)
    sync_type = Column(String(50), nullable=False)
    status = Column(String(20), nullable=False)
    details = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, sync_type: str, status: str, details: str = None):
        self.sync_type = sync_type
        self.status = status
        self.details = details