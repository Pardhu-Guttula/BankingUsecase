# Epic Title: Role-based Access Control

from sqlalchemy import Table, Column, Integer, ForeignKey
from backend.app import db

role_permissions = Table('role_permissions', db.Model.metadata,
    Column('role_id', Integer, ForeignKey('roles.id'), primary_key=True),
    Column('permission_id', Integer, ForeignKey('permissions.id'), primary_key=True)
)

# File 3: Permission Repository in repositories/access_control/permission_repository.py