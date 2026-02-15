# Epic Title: Role-based Access Control

from sqlalchemy import Table, Column, Integer, ForeignKey
from backend.app import db

roles_permissions = Table(
    'roles_permissions',
    db.Model.metadata,
    Column('role_id', Integer, ForeignKey('roles.id')),
    Column('permission_id', Integer, ForeignKey('permissions.id'))
)


# File 3: Update Role Model to Include Permissions Relationship in models/access_control/role_model.py