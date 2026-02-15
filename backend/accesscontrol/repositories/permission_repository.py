# Epic Title: Assign Permissions to Roles

from backend.accesscontrol.models.permission_model import Permission
from backend.app import db

class PermissionRepository:
    @staticmethod
    def save(permission: Permission) -> None:
        db.session.add(permission)
        db.session.commit()

    @staticmethod
    def get_by_id(permission_id: int) -> Permission:
        return Permission.query.get(permission_id)

    @staticmethod
    def get_all() -> list[Permission]:
        return Permission.query.all()


# File 4: RolePermission Repository for Database Operations in accesscontrol/repositories/role_permission_repository.py