# Epic Title: Role-based Access Control

from sqlalchemy import Column, Integer, ForeignKey, Table
from backend.app import db

role_permission = Table('role_permission', db.Model.metadata,
    Column('role_id', Integer, ForeignKey('roles.id'), primary_key=True),
    Column('permission_id', Integer, ForeignKey('permissions.id'), primary_key=True)
)


# File 3: Update Role Model to Include Permissions Relationship in authentication/models/role_model.py