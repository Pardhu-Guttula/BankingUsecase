# Epic Title: Role-based Access Control

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from backend.app import db

class Policy(db.Model):
    __tablename__ = 'policies'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255), nullable=True)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    role = relationship('Role', back_populates='policies')

    def __init__(self, name: str, description: str, role_id: int, is_active: bool = True):
        self.name = name
        self.description = description
        self.role_id = role_id
        self.is_active = is_active


# File 2: Update Role Model to Include Relationship with Policy in models/access_control/role_model.py