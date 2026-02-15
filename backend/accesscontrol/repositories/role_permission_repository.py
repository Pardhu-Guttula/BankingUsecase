# Epic Title: Assign Permissions to Roles

from backend.accesscontrol.models.role_permission_model import RolePermission
from backend.app import db

class RolePermissionRepository:
    @staticmethod
    def save(role_permission: RolePermission) -> None:
        db.session.add(role_permission)
        db.session.commit()

    @staticmethod
    def get_by_role_id(role_id: int) -> list[RolePermission]:
        return RolePermission.query.filter_by(role_id=role_id).all()


# File 5: Permission Service for Business Logic in accesscontrol/services/permission_service.py