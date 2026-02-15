# Epic Title: Role-based Access Control

from backend.models.access_control.role_permission_model import RolePermission
from backend.app import db

class RolePermissionRepository:
    @staticmethod
    def assign_permission_to_role(role_id: int, permission_id: int) -> None:
        role_permission = RolePermission(role_id=role_id, permission_id=permission_id)
        db.session.add(role_permission)
        db.session.commit()

    @staticmethod
    def remove_permission_from_role(role_id: int, permission_id: int) -> None:
        role_permission = RolePermission.query.filter_by(role_id=role_id, permission_id=permission_id).first()
        if role_permission:
            db.session.delete(role_permission)
            db.session.commit()


# File 5: Permission Service for Business Logic in access_control/services/permission_service.py