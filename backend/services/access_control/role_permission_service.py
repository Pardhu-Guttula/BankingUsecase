# Epic Title: Assign Permissions to Roles

from backend.repositories.access_control.role_permission_repository import RolePermissionRepository
from backend.models.access_control.role_permission_model import RolePermission

class RolePermissionService:
    @staticmethod
    def assign_permission_to_role(role_id: int, permission_id: int) -> None:
        role_permission = RolePermission(role_id=role_id, permission_id=permission_id)
        RolePermissionRepository.save(role_permission)

    @staticmethod
    def remove_permission_from_role(role_id: int, permission_id: int) -> None:
        role_permissions = RolePermissionRepository.find_by_role_id(role_id)
        for role_permission in role_permissions:
            if role_permission.permission_id == permission_id:
                RolePermissionRepository.delete(role_permission)
                break

    @staticmethod
    def get_permissions_by_role(role_id: int) -> list[RolePermission]:
        return RolePermissionRepository.find_by_role_id(role_id)


# File 6: Permission Controller in `controllers/access_control/permission_controller.py`