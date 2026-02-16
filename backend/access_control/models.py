# Epic Title: Role-based Access Control

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Role(db.Model):
    __tablename__ = "roles"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(50), unique=True, nullable=False)
    description: str = db.Column(db.String(255), nullable=True)
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Role {self.name}>"

class UserRole(db.Model):
    __tablename__ = "user_roles"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    role_id: int = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False)
    assigned_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<UserRole user_id={self.user_id} role_id={self.role_id}>"

class Permission(db.Model):
    __tablename__ = "permissions"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(50), unique=True, nullable=False)
    description: str = db.Column(db.String(255), nullable=True)
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Permission {self.name}>"

class RolePermission(db.Model):
    __tablename__ = "role_permissions"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_id: int = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False)
    permission_id: int = db.Column(db.Integer, db.ForeignKey("permissions.id"), nullable=False)
    assigned_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<RolePermission role_id={self.role_id} permission_id={self.permission_id}>"