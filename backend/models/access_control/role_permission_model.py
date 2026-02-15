# Epic Title: Role-based Access Control

from sqlalchemy import Column, Integer, ForeignKey
from backend.app import db

class RolePermission(db.Model):
    __tablename__ = 'role_permissions'

    role_id = Column(Integer, ForeignKey('roles.id'), primary_key=True)
    permission_id = Column(Integer, ForeignKey('permissions.id'), primary_key=True)

    def __init__(self, role_id: int, permission_id: int):
        self.role_id = role_id
        self.permission_id = permission_id


# File 3: Permission Repository for CRUD Operations in access_control/roles/permission_repository.py