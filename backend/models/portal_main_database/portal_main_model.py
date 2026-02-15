# Epic Title: Core Banking System Integration

from sqlalchemy import Column, Integer, String, DateTime
from backend.app import db
from datetime import datetime

class PortalMainModel(db.Model):
    __tablename__ = 'portal_main'

    id = Column(Integer, primary_key=True)
    data = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, data: str):
        self.data = data

# File 2: Portal Database Repository in repositories/portal_main_database/portal_main_repository.py