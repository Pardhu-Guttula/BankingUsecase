# Epic Title: User Authentication and Security

from sqlalchemy import Column, Integer, String, Boolean
from backend.app import db

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    is_2fa_enabled = Column(Boolean, default=False)

    def __init__(self, username: str, password_hash: str, email: str, is_2fa_enabled: bool = False):
        self.username = username
        self.password_hash = password_hash
        self.email = email
        self.is_2fa_enabled = is_2fa_enabled


# File 2: Two-Factor Authentication Model in models/authentication/two_factor_model.py