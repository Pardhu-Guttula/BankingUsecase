# Epic Title: Manage Secure Storage of Credentials

from sqlalchemy import Column, Integer, String, create_engine, Boolean
from sqlalchemy.orm import declarative_base, relationship
from werkzeug.security import generate_password_hash, check_password_hash

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    is_active = Column(Boolean, default=True)
    mfa_enabled = Column(Boolean, default=False)

    sessions = relationship('Session', back_populates='user')

    # Store secure hashed password
    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def __repr__(self) -> str:
        return f"<User(username='{self.username}', is_active='{self.is_active}', mfa_enabled='{self.mfa_enabled}')>"



# File 2: Update Session Model for Secure Storage in authentication/models/session.py