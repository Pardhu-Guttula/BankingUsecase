# Epic Title: Role-based Access Control

from sqlalchemy import Column, Integer, String, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app import db
from backend.models.access_control.role_permission import roles_permissions

roles_users = Table(
    'roles_users',
    db.Column('user_id', Integer, db.ForeignKey('users.id')),
    db.Column('role_id', Integer, db.ForeignKey('roles.id'))
)

class Role(db.Model):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    users = relationship("User", secondary=roles_users, back_populates="roles")
    permissions = relationship("Permission", secondary=roles_permissions, back_populates="roles")
    policies = relationship("Policy", back_populates="role")

    def __init__(self, name: str, description: str = None):
        self.name = name
        self.description = description


# File 3: Policy Repository to Manage Policies in repositories/access_control/policy_repository.py