# Epic Title: Role-based Access Control

from backend.repositories.access_control.role_repository import RoleRepository
from backend.repositories.access_control.permission_repository import PermissionRepository
from backend.models.access_control.role_model import Role
from backend.models.access_control.permission_model import Permission

class RoleService:
    @staticmethod
    def create_role(name: str, description: str = None) -> Role:
        role = Role(name, description)
        RoleRepository.save(role)
        return role

    @staticmethod
    def assign_permission_to_role(role_id: int, permission_id: int) -> None:
        role = RoleRepository.find_by_id(role_id)
        permission = PermissionRepository.find_by_id(permission_id)
        if role and permission:
            role.permissions.append(permission)
            RoleRepository.save(role)

    @staticmethod
    def get_all_roles() -> list[Role]:
        return RoleRepository.find_all()

    @staticmethod
    def get_all_permissions() -> list[Permission]:
        return PermissionRepository.find_all()


# File 7: Permission Form to Capture Permission Data in forms/permission_form.py