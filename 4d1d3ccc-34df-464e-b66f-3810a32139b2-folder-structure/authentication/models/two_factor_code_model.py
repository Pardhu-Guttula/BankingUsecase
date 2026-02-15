# Epic Title: Implement Secure Login Mechanism

from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from backend.app import db

class TwoFactorCode(db.Model):
    __tablename__ = 'two_factor_codes'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    code = Column(String(6), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, user_id: int, code: str):
        self.user_id = user_id
        self.code = code


# File 4: Two-Factor Code Repository for Database Operations in authentication/repositories/two_factor_code_repository.py