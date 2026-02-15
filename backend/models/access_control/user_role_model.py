# Epic Title: Role-based Access Control

from sqlalchemy import Column, Integer, ForeignKey
from backend.app import db

class UserRole(db.Model):
    __tablename__ = 'user_roles'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    role_id = Column(Integer, ForeignKey('roles.id'), primary_key=True)

    def __init__(self, user_id: int, role_id: int):
        self.user_id = user_id
        self.role_id = role_id


# File 3: Role Repository for CRUD Operations in access_control/roles/role_repository.py