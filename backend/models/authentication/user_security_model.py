# Epic Title: User Authentication and Security

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.app import db
import datetime

class UserSecurity(db.Model):
    __tablename__ = 'user_security'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    otp_secret = Column(String(16), nullable=False)
    is_otp_enabled = Column(String(5), default='False', nullable=False)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    user = relationship('User', back_populates='security_bag')

    def __init__(self, user_id: int, otp_secret: str, is_otp_enabled: bool = False):
        self.user_id = user_id
        self.otp_secret = otp_secret
        self.is_otp_enabled = is_otp_enabled


# File 2: Update User Model to Include Relationship with User Security in models/authentication/user_model.py