# Epic Title: Role-based Access Control

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.app import db

class Permission(db.Model):
    __tablename__ = 'permissions'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255), nullable=True)

    roles = relationship('RolePermission', back_populates='permission')

    def __init__(self, name: str, description: str = ''):
        self.name = name
        self.description = description


# File 2: RolePermission Model to Define Many-to-Many Relationship in models/access_control/role_permission_model.py