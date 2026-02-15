# Epic Title: Assign Permissions to Roles

from backend.accesscontrol.repositories.permission_repository import PermissionRepository
from backend.accesscontrol.repositories.role_permission_repository import RolePermissionRepository
from backend.accesscontrol.models.permission_model import Permission
from backend.accesscontrol.models.role_permission_model import RolePermission

class PermissionService:
    @staticmethod
    def create_permission(name: str) -> Permission:
        permission = Permission(name=name)
        PermissionRepository.save(permission)
        return permission

    @staticmethod
    def assign_permission_to_role(role_id: int, permission_id: int) -> None:
        role_permission = RolePermission(role_id=role_id, permission_id=permission_id)
        RolePermissionRepository.save(role_permission)

    @staticmethod
    def get_all_permissions() -> list[Permission]:
        return PermissionRepository.get_all()

    @staticmethod
    def get_permissions_for_role(role_id: int) -> list[RolePermission]:
        return RolePermissionRepository.get_by_role_id(role_id)


# File 6: Permission Controller for Handling Requests in accesscontrol/controllers/permission_controller.py