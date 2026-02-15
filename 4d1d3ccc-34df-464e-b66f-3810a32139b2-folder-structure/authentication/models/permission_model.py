# Epic Title: Role-based Access Control

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app import db
from authentication.models.role_permission_model import role_permission

class Permission(db.Model):
    __tablename__ = 'permissions'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    roles = relationship("Role", secondary=role_permission, back_populates="permissions")

    def __init__(self, name: str, description: str = None):
        self.name = name
        self.description = description


# File 5: Permission Repository for Database Operations in authentication/repositories/permission_repository.py