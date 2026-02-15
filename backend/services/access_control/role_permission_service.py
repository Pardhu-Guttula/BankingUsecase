# Epic Title: Role-based Access Control

from backend.repositories.access_control.role_permission_repository import RolePermissionRepository

class RolePermissionService:
    @staticmethod
    def assign_permission(role_id: int, permission_id: int) -> None:
        RolePermissionRepository.assign_permission_to_role(role_id, permission_id)

    @staticmethod
    def remove_permission(role_id: int, permission_id: int) -> None:
        RolePermissionRepository.remove_permission_from_role(role_id, permission_id)


# File 7: Permission Controller in access_control/controllers/permission_controller.py