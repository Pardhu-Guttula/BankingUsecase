# Epic Title: Role-based Access Control

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from backend.app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(150), unique=True, nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey('roles.id'))
    role = relationship("Role", back_populates="users")

    def __init__(self, username: str, email: str, password: str, is_admin: bool = False):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.is_active = True
        self.is_admin = is_admin

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def has_permission(self, permission_name: str) -> bool:
        if self.role:
            return any(perm.name == permission_name for perm in self.role.permissions)
        return False

Role.users = relationship("User", order_by=User.id, back_populates="role")

# File 7: Register Role Controller Blueprint in app.py (Already Exists, Modified)