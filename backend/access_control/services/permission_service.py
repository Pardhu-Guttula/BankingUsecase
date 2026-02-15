# Epic Title: Role-based Access Control

from backend.access_control.roles.permission_repository import PermissionRepository
from backend.access_control.roles.role_permission_repository import RolePermissionRepository
from backend.models.access_control.permission_model import Permission
from flask import current_app

class PermissionService:
    @staticmethod
    def create_permission(name: str, description: str = None) -> bool:
        if PermissionRepository.get_permission_by_name(name):
            return False
        new_permission = Permission(name=name, description=description)
        PermissionRepository.save(new_permission)
        return True

    @staticmethod
    def get_all_permissions() -> list[Permission]:
        return PermissionRepository.get_all_permissions()

    @staticmethod
    def assign_permission(role_id: int, permission_id: int) -> None:
        RolePermissionRepository.assign_permission_to_role(role_id, permission_id)

    @staticmethod
    def remove_permission(role_id: int, permission_id: int) -> None:
        RolePermissionRepository.remove_permission_from_role(role_id, permission_id)


# File 6: Permission Controller to Expose Endpoints for Permission Management in access_control/controllers/permission_controller.py