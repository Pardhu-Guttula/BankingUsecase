# Epic Title: Role-based Access Control

from backend.models.access_control.permission_model import Permission
from backend.app import db

class PermissionRepository:
    @staticmethod
    def get_all_permissions() -> list[Permission]:
        return Permission.query.all()

    @staticmethod
    def get_permission_by_id(permission_id: int) -> Permission:
        return Permission.query.get(permission_id)

    @staticmethod
    def save(permission: Permission) -> None:
        db.session.add(permission)
        db.session.commit()

    @staticmethod
    def update(permission: Permission) -> None:
        db.session.commit()

    @staticmethod
    def delete(permission: Permission) -> None:
        db.session.delete(permission)
        db.session.commit()


# File 5: RolePermission Repository for CRUD Operations in repositories/access_control/role_permission_repository.py