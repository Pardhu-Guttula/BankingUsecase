# Epic Title: Role-based Access Control

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from backend.app import db

class RolePermission(db.Model):
    __tablename__ = 'role_permissions'

    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)
    permission_id = Column(Integer, ForeignKey('permissions.id'), nullable=False)

    role = relationship('Role', back_populates='permissions')
    permission = relationship('Permission', back_populates='roles')


# File 3: Update Role Model to Include Relationship with Permission in models/access_control/role_model.py