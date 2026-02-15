# Epic Title: Implement Secure Login Mechanism

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime
from backend.app import db

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone_number = Column(String(15), unique=True, nullable=False)
    two_factor_enabled = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, username: str, password_hash: str, email: str, phone_number: str, two_factor_enabled: bool):
        self.username = username
        self.password_hash = password_hash
        self.email = email
        self.phone_number = phone_number
        self.two_factor_enabled = two_factor_enabled


# File 2: User Repository for Database Operations in authentication/repositories/user_repository.py