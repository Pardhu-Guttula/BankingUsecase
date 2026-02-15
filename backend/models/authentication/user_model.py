# Epic Title: User Authentication and Security

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from backend.app import db

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    mfa_enabled = Column(Boolean, default=False)
    mfa_secret = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, username: str, email: str, password_hash: str, mfa_enabled: bool = False, mfa_secret: str = None):
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.mfa_enabled = mfa_enabled
        self.mfa_secret = mfa_secret

# File 3: User Repository in repositories/authentication/user_repository.py (Already exists, Modified)