# Epic Title: Manage Secure Storage of Credentials

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime, timedelta
from cryptography.fernet import Fernet

Base = declarative_base()

class Session(Base):
    __tablename__ = 'sessions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    token = Column(String(256), unique=True, nullable=False)
    created_at = Column(DateTime, default=func.now())
    last_activity = Column(DateTime, default=func.now())

    user = relationship('User', back_populates='sessions')

    def is_expired(self, current_time: datetime) -> bool:
        return current_time - self.last_activity > timedelta(minutes=15)

    def update_activity(self, current_time: datetime):
        self.last_activity = current_time

    def __repr__(self) -> str:
        return f"<Session(user_id='{self.user_id}', token='{self.token}', created_at='{self.created_at}', last_activity='{self.last_activity}')>"

    # Token encryption method
    @staticmethod
    def encrypt_token(token: str, key: bytes) -> str:
        fernet = Fernet(key)
        encrypted_token = fernet.encrypt(token.encode())
        return encrypted_token.decode()

    @staticmethod
    def decrypt_token(encrypted_token: str, key: bytes) -> str:
        fernet = Fernet(key)
        token = fernet.decrypt(encrypted_token.encode()).decode()
        return token



# File 3: Authentication Service Update for Secure Storage in authentication/services/auth_service.py