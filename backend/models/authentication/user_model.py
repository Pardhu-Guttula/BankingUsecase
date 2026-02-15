# Epic Title: Implement Secure Login Mechanism

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from backend.app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from backend.services.authentication.mfa_service import MFAService

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(150), unique=True, nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    mfa_secret = Column(String(32), nullable=False)

    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.is_active = True
        self.created_at = datetime.utcnow()
        self.mfa_secret = MFAService.generate_secret()

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)


# File 2: User Repository in repositories/authentication/user_repository.py