# Epic Title: Role-based Access Control

from backend.models.access_control.permission_model import Permission
from backend.app import db

class PermissionRepository:
    @staticmethod
    def save(permission: Permission) -> None:
        db.session.add(permission)
        db.session.commit()

    @staticmethod
    def get_all_permissions() -> list[Permission]:
        return Permission.query.all()

    @staticmethod
    def get_permission_by_name(permission_name: str) -> Permission:
        return Permission.query.filter_by(name=permission_name).first()

    @staticmethod
    def delete(permission: Permission) -> None:
        db.session.delete(permission)
        db.session.commit()


# File 4: RolePermission Repository to Associate Roles and Permissions in access_control/roles/role_permission_repository.py