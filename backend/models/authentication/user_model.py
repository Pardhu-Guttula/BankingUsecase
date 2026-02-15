# Epic Title: User Authentication and Security

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from werkzeug.security import generate_password_hash, check_password_hash
from backend.app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    mfa_enabled = Column(Boolean, default=False)
    mfa_secret = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, username: str, email: str, password: str, mfa_enabled: bool = False, mfa_secret: str = None):
        self.username = username
        self.email = email
        self.set_password(password)  # Securely set the password
        self.mfa_enabled = mfa_enabled
        self.mfa_secret = mfa_secret
        
    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

# File 2: User Repository for Secure Storage and Retrieval in repositories/authentication/user_repository.py