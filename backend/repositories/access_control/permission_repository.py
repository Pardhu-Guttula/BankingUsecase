# Epic Title: Assign Permissions to Roles

from backend.models.access_control.permission_model import Permission
from backend.app import db

class PermissionRepository:
    @staticmethod
    def save(permission: Permission) -> None:
        db.session.add(permission)
        db.session.commit()

    @staticmethod
    def find_by_id(permission_id: int) -> Permission:
        return Permission.query.filter_by(id=permission_id).first()

    @staticmethod
    def find_all() -> list[Permission]:
        return Permission.query.all()


# File 4: RolePermission Repository in `repositories/access_control/role_permission_repository.py`