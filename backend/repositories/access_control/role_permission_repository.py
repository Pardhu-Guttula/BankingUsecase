# Epic Title: Assign Permissions to Roles

from backend.models.access_control.role_permission_model import RolePermission
from backend.app import db

class RolePermissionRepository:
    @staticmethod
    def save(role_permission: RolePermission) -> None:
        db.session.add(role_permission)
        db.session.commit()

    @staticmethod
    def delete(role_permission: RolePermission) -> None:
        db.session.delete(role_permission)
        db.session.commit()

    @staticmethod
    def find_by_role_id(role_id: int) -> list[RolePermission]:
        return RolePermission.query.filter_by(role_id=role_id).all()


# File 5: RolePermission Service in `services/access_control/role_permission_service.py`