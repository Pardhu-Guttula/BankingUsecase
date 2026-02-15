# Epic Title: Role-based Access Control

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app import db

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    role = relationship("Role", back_populates="users")

    def __init__(self, username: str, password: str, email: str, role_id: int):
        self.username = username
        self.password = password
        self.email = email
        self.role_id = role_id


# File 3: Role Repository for Database Operations in authentication/repositories/role_repository.py