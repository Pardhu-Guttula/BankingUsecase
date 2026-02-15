# Epic Title: Personalized Dashboard

from sqlalchemy import Column, Integer, String, DateTime, Boolean, LargeBinary
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app import db

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    mfa_enabled = Column(Boolean, default=False)
    mfa_secret = Column(String(32), nullable=True)
    session_key = Column(LargeBinary, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    roles = relationship("Role", back_populates="users")
    accounts = relationship("Account", back_populates="user")

    def __init__(self, username: str, password: str, email: str, mfa_enabled: bool = False, mfa_secret: str = None, session_key: bytes = None):
        self.username = username
        self.password = password
        self.email = email
        self.mfa_enabled = mfa_enabled
        self.mfa_secret = mfa_secret
        self.session_key = session_key


# File 4: Account Repository for Account Operations in repositories/accounts/account_repository.py