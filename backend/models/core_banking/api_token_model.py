# Epic Title: Core Banking System Integration

from sqlalchemy import Column, Integer, String, DateTime
from backend.app import db
import datetime

class APIToken(db.Model):
    __tablename__ = 'api_tokens'

    id = Column(Integer, primary_key=True)
    token = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    expires_at = Column(DateTime, nullable=False)

    def __init__(self, token: str, expires_at: datetime.datetime):
        self.token = token
        self.expires_at = expires_at


# File 2: Core Banking Repository to Handle Token CRUD Operations in integration/repositories/api_token_repository.py