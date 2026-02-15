# Epic Title: Role-based Access Control

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app import db
from authentication.models.role_permission_model import role_permission

class Role(db.Model):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    users = relationship("User", back_populates="role")
    permissions = relationship("Permission", secondary=role_permission, back_populates="roles")

    def __init__(self, name: str, description: str = None):
        self.name = name
        self.description = description


# File 4: Update Permission Model to Include Roles Relationship in authentication/models/permission_model.py