# Epic Title: Role-based Access Control

from backend.models.access_control.permission_model import Permission
from backend.app import db

class PermissionRepository:
    @staticmethod
    def save(permission: Permission) -> None:
        db.session.add(permission)
        db.session.commit()

    @staticmethod
    def find_all() -> list[Permission]:
        return Permission.query.all()

    @staticmethod
    def find_by_name(name: str) -> Permission | None:
        return Permission.query.filter_by(name=name).first()

# File 4: Role Service Updated for Permission Assignment in services/access_control/role_service.py (Modified)