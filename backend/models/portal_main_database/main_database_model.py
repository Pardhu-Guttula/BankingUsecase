# Epic Title: Core Banking System Integration

from sqlalchemy import Column, Integer, String, DateTime, Float
from datetime import datetime
from backend.app import db

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        self.created_at = datetime.utcnow()

# File 2: Core Banking Synchronization Logic in services/integration/core_banking_synch_service.py (Refactored for Middleware)