# Epic Title: Role-based Access Control

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.app import db

class Role(db.Model):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255), nullable=True)

    users = relationship('User', back_populates='role')
    permissions = relationship('RolePermission', back_populates='role')
    policies = relationship('Policy', back_populates='role')

    def __init__(self, name: str, description: str = ''):
        self.name = name
        self.description = description


# File 3: Policy Repository for CRUD Operations in repositories/access_control/policy_repository.py