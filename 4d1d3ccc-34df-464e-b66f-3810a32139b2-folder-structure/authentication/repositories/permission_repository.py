# Epic Title: Role-based Access Control

from authentication.models.permission_model import Permission
from backend.app import db

class PermissionRepository:
    @staticmethod
    def save(permission: Permission) -> None:
        db.session.add(permission)
        db.session.commit()

    @staticmethod
    def get_all() -> list[Permission]:
        return Permission.query.all()

    @staticmethod
    def get_by_id(permission_id: int) -> Permission:
        return Permission.query.get(permission_id)


# File 6: Role Service Update to Handle Permissions in authentication/services/role_service.py