# Epic Title: User Authentication and Security

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from backend.app import db
import datetime

class TwoFactorAuth(db.Model):
    __tablename__ = 'two_factor_auth'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    otp_secret = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    def __init__(self, user_id: int, otp_secret: str):
        self.user_id = user_id
        self.otp_secret = otp_secret


# File 3: User Repository Handling Login and 2FA in authentication/repositories/user_repository.py