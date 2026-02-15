# Epic Title: Implement Secure Login Mechanism

from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.types import Boolean

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    is_active = Column(Boolean, default=True)
    # Implement secure login mechanism with multi-factor authentication
    mfa_enabled = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"<User(username='{self.username}', is_active='{self.is_active}', mfa_enabled='{self.mfa_enabled}')>"



# File 2: Session Model in authentication/models/session.py