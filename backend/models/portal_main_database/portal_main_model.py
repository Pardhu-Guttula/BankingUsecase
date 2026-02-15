# Epic Title: Maintain Separate Database

from sqlalchemy import Column, Integer, String, DateTime
from backend.app import db
from datetime import datetime

class PortalMainData(db.Model):
    __tablename__ = 'portal_main_data'

    id = Column(Integer, primary_key=True)
    data_key = Column(String(255), nullable=False)
    data_value = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, data_key: str, data_value: str):
        self.data_key = data_key
        self.data_value = data_value
        self.created_at = datetime.utcnow()


# File 2: Portal Main Database Repository in `repositories/portal_main_database/portal_main_repository.py`