# Epic Title: Role-based Access Control

from authentication.repositories.permission_repository import PermissionRepository
from authentication.models.permission_model import Permission

class PermissionService:
    @staticmethod
    def define_permission(name: str, description: str = None) -> Permission:
        permission = Permission(name, description)
        PermissionRepository.save(permission)
        return permission

    @staticmethod
    def get_all_permissions() -> list[Permission]:
        return PermissionRepository.get_all()


# File 8: Role Controller Update to Handle Permissions in authentication/controllers/role_controller.py