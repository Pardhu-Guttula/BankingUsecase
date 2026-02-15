# Epic Title: User Authentication and Security

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from backend.app import db
from werkzeug.security import generate_password_hash, check_password_hash
from cryptography.fernet import Fernet

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    is_2fa_enabled = Column(Boolean, default=False)
    encryption_key = Column(String(44), nullable=False)
    encrypted_credentials = Column(String(255), nullable=True)
    mfa_secret = Column(String(16), nullable=True)

    documents = relationship('Document', back_populates='user')
    accounts = relationship('Account', back_populates='user')
    widgets = relationship('Widget', back_populates='user')
    service_modifications = relationship('ServiceModification', back_populates='user')
    statuses = relationship('RequestStatus', back_populates='user')
    approvals = relationship('RequestApproval', back_populates='approver')
    email_notifications = relationship('EmailNotification', back_populates='user')
    in_app_notifications = relationship('InAppNotification', back_populates='user')
    interactions = relationship('InteractionHistory', back_populates='user')
    transactions = relationship('Transaction', back_populates='user')
    security_bag = relationship('UserSecurity', back_populates='user', uselist=False)
    account_opening_requests = relationship('AccountOpeningRequest', back_populates='user')

    def __init__(self, username: str, password: str, email: str, is_2fa_enabled: bool = False):
        self.username = username
        self.password_hash = self._generate_password_hash(password)
        self.email = email
        self.is_2fa_enabled = is_2fa_enabled
        self.encryption_key = Fernet.generate_key().decode()
        self.encrypted_credentials = self._encrypt_credentials(password)

    @staticmethod
    def _generate_password_hash(password: str) -> str:
        return generate_password_hash(password)

    def _encrypt_credentials(self, plain_text: str) -> str:
        f = Fernet(self.encryption_key)
        return f.encrypt(plain_text.encode()).decode()

    def verify_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def get_decrypted_credentials(self) -> str:
        f = Fernet(self.encryption_key)
        return f.decrypt(self.encrypted_credentials.encode()).decode()


# File 2: Authentication Service with Multi-Factor Authentication Logic in services/authentication/authentication_service.py