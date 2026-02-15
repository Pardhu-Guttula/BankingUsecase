# Epic Title: User Authentication and Security

from sqlalchemy import Column, Integer, String, DateTime, Boolean, LargeBinary
from datetime import datetime
from backend.app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    mfa_enabled = Column(Boolean, default=False)
    mfa_secret = Column(String(32), nullable=True)
    session_key = Column(LargeBinary, nullable=True)
    last_activity = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    def __init__(self, username: str, password: str, email: str, mfa_enabled: bool = False, mfa_secret: str = None, session_key: bytes = None):
        self.username = username
        self.email = email
        self.mfa_enabled = mfa_enabled
        self.mfa_secret = mfa_secret
        self.session_key = session_key
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)


# File 3: Modify Authentication Service to Handle Session Expiry in auth/services/authentication_service.py