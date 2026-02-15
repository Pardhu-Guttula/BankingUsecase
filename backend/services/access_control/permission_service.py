# Epic Title: Role-based Access Control

from backend.models.access_control.permission_model import Permission
from backend.models.access_control.role_permission_model import RolePermission
from backend.repositories.access_control.permission_repository import PermissionRepository
from backend.repositories.access_control.role_permission_repository import RolePermissionRepository

class PermissionService:
    @staticmethod
    def create_permission(name: str, description: str = None) -> Permission:
        permission = Permission(name=name, description=description)
        PermissionRepository.save(permission)
        return permission

    @staticmethod
    def assign_permission_to_role(role_id: int, permission_id: int) -> RolePermission:
        role_permission = RolePermission(role_id=role_id, permission_id=permission_id)
        RolePermissionRepository.save(role_permission)
        return role_permission

    @staticmethod
    def get_permissions() -> list[Permission]:
        return PermissionRepository.get_all()

    @staticmethod
    def get_role_permissions(role_id: int) -> list[RolePermission]:
        return RolePermissionRepository.get_permissions_by_role(role_id)

# File 6: Permission Management Controller in rbac/controllers/permission_controller.py