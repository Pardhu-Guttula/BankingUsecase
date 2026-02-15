# Epic Title: Core Banking System Integration

from sqlalchemy import Column, Integer, String, DateTime
from backend.app import db
import datetime

class IntegrationSettings(db.Model):
    __tablename__ = 'integration_settings'

    id = Column(Integer, primary_key=True)
    core_banking_api_url = Column(String(255), nullable=False)
    core_banking_api_key = Column(String(255), nullable=False)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    def __init__(self, core_banking_api_url: str, core_banking_api_key: str):
        self.core_banking_api_url = core_banking_api_url
        self.core_banking_api_key = core_banking_api_key
        self.last_updated = datetime.datetime.utcnow()


# File 2: Integration Settings Repository to Handle CRUD Operations in integration/repositories/integration_settings_repository.py