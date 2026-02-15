# Epic Title: Role-based Access Control

from sqlalchemy import Column, Integer, String, DateTime, Boolean, LargeBinary
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app import db
from backend.models.access_control.role_model import roles_users

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    mfa_enabled = Column(Boolean, default=False)
    mfa_secret = Column(String(32), nullable=True)
    session_key = Column(LargeBinary, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    roles = relationship("Role", secondary=roles_users, back_populates="users")
    accounts = relationship("Account", back_populates="user")
    account_opening_requests = relationship("AccountOpeningRequest", back_populates="user")
    service_modification_requests = relationship("ServiceModificationRequest", back_populates="user")
    status_updates = relationship("StatusUpdate", back_populates="user")
    interactions = relationship("Interaction", back_populates="user")
    documents = relationship("Document", back_populates="user")
    applications = relationship("Application", back_populates="user")

    def __init__(self, username: str, password: str, email: str, mfa_enabled: bool = False, mfa_secret: str = None, session_key: bytes = None):
        self.username = username
        self.password = password
        self.email = email
        self.mfa_enabled = mfa_enabled
        self.mfa_secret = mfa_secret
        self.session_key = session_key


# File 5: Permission Repository to Manage Permissions in repositories/access_control/permission_repository.py