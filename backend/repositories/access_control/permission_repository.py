# Epic Title: Role-based Access Control

from backend.models.access_control.permission_model import Permission
from backend.app import db

class PermissionRepository:
    @staticmethod
    def save(permission: Permission) -> None:
        db.session.add(permission)
        db.session.commit()

    @staticmethod
    def find_by_id(permission_id: int) -> Permission:
        return Permission.query.get(permission_id)

    @staticmethod
    def find_by_name(name: str) -> Permission:
        return Permission.query.filter_by(name=name).first()

    @staticmethod
    def find_all() -> list[Permission]:
        return Permission.query.all()


# File 6: Role Service to Assign Permissions in services/access_control/role_service.py