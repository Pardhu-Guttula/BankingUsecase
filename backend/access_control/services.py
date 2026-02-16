# Epic Title: Role-based Access Control

import logging
from flask_sqlalchemy import SQLAlchemy
from backend.access_control.models import Role, UserRole, Permission, RolePermission

logger = logging.getLogger(__name__)

class RoleService:
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def create_role(self, name: str, description: str = "") -> Role:
        if Role.query.filter_by(name=name).first():
            raise ValueError(f"Role with name '{name}' already exists.")
        role = Role(name=name, description=description)
        self.db.session.add(role)
        self.db.session.commit()
        logger.info(f"Created role: {role}")
        return role

    def assign_role_to_user(self, user_id: int, role_id: int) -> UserRole:
        if UserRole.query.filter_by(user_id=user_id, role_id=role_id).first():
            raise ValueError(f"User {user_id} already has role {role_id}.")
        user_role = UserRole(user_id=user_id, role_id=role_id)
        self.db.session.add(user_role)
        self.db.session.commit()
        logger.info(f"Assigned role {role_id} to user {user_id}")
        return user_role

    def create_permission(self, name: str, description: str = "") -> Permission:
        if Permission.query.filter_by(name=name).first():
            raise ValueError(f"Permission with name '{name}' already exists.")
        permission = Permission(name=name, description=description)
        self.db.session.add(permission)
        self.db.session.commit()
        logger.info(f"Created permission: {permission}")
        return permission

    def assign_permission_to_role(self, role_id: int, permission_id: int) -> RolePermission:
        if RolePermission.query.filter_by(role_id=role_id, permission_id=permission_id).first():
            raise ValueError(f"Role {role_id} already has permission {permission_id}.")
        role_permission = RolePermission(role_id=role_id, permission_id=permission_id)
        self.db.session.add(role_permission)
        self.db.session.commit()
        logger.info(f"Assigned permission {permission_id} to role {role_id}")
        return role_permission

    def get_roles(self) -> list[Role]:
        return Role.query.all()

    def get_permissions(self) -> list[Permission]:
        return Permission.query.all()

    def get_role_permissions(self, role_id: int) -> list[RolePermission]:
        return RolePermission.query.filter_by(role_id=role_id).all()

    def get_user_roles(self, user_id: int) -> list[UserRole]:
        return UserRole.query.filter_by(user_id=user_id).all()

    def get_user_permissions(self, user_id: int) -> list[Permission]:
        roles = self.get_user_roles(user_id)
        permissions = []
        for user_role in roles:
            role_permissions = self.get_role_permissions(user_role.role_id)
            for role_permission in role_permissions:
                permission = Permission.query.get(role_permission.permission_id)
                permissions.append(permission)
        return permissions