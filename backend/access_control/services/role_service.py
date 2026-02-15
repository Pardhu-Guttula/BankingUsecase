# Epic Title: Role-based Access Control

from backend.access_control.roles.role_repository import RoleRepository
from backend.access_control.roles.user_role_repository import UserRoleRepository
from backend.models.access_control.role_model import Role
from flask import current_app

class RoleService:
    @staticmethod
    def create_role(name: str, description: str = None) -> bool:
        if RoleRepository.get_role_by_name(name):
            return False
        new_role = Role(name=name, description=description)
        RoleRepository.save(new_role)
        return True

    @staticmethod
    def get_all_roles() -> list[Role]:
        return RoleRepository.get_all_roles()

    @staticmethod
    def assign_role(user_id: int, role_id: int) -> None:
        UserRoleRepository.assign_role_to_user(user_id, role_id)

    @staticmethod
    def remove_role(user_id: int, role_id: int) -> None:
        UserRoleRepository.remove_role_from_user(user_id, role_id)


# File 6: Role Controller to Expose Endpoints for Role Management in access/controllers/role_controller.py