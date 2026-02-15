# Epic Title: User Authentication and Security

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from datetime import datetime
from backend.app import db


class MFA(db.Model):
    __tablename__ = 'mfa'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    secret = Column(String(64), nullable=False)
    confirmed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, user_id: int, secret: str, confirmed: bool = False, created_at: DateTime = None):
        self.user_id = user_id
        self.secret = secret
        self.confirmed = confirmed
        if created_at is None:
            created_at = datetime.utcnow()
        self.created_at = created_at


# File 2: MFA Repository for Data Access in repositories/authentication/mfa_repository.py