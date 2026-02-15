# Epic Title: Real-time Status Updates and Notifications

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from backend.app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    is_2fa_enabled = Column(Boolean, default=False)

    accounts = relationship('Account', back_populates='user')
    widgets = relationship('Widget', back_populates='user')
    service_modifications = relationship('ServiceModification', back_populates='user')
    statuses = relationship('RequestStatus', back_populates='user')
    approvals = relationship('RequestApproval', back_populates='approver')

    def __init__(self, username: str, password: str, email: str, is_2fa_enabled: bool = False):
        self.username = username
        self.password_hash = self._generate_password_hash(password)
        self.email = email
        self.is_2fa_enabled = is_2fa_enabled

    @staticmethod
    def _generate_password_hash(password: str) -> str:
        return generate_password_hash(password)

    def verify_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)


# File 3: Status Repository for CRUD Operations in repositories/status/request_status_repository.py