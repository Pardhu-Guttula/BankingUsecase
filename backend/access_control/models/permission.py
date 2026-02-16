# Epic Title: Role-based Access Control

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Permission(db.Model):
    __tablename__ = "permissions"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Permission {self.name}>"

class RolePermission(db.Model):
    __tablename__ = "role_permissions"

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), primary_key=True)
    permission_id = db.Column(db.Integer, db.ForeignKey('permissions.id'), primary_key=True)
    assigned_at = db.Column(db.DateTime, default=datetime.utcnow)

    role = db.relationship('Role', back_populates='permissions')
    permission = db.relationship('Permission', back_populates='roles')

Role.permissions = db.relationship('RolePermission', order_by=RolePermission.permission_id, back_populates='role')
Permission.roles = db.relationship('RolePermission', order_by=RolePermission.role_id, back_populates='permission')