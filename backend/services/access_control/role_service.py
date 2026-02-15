# Epic Title: Role-based Access Control

from backend.repositories.access_control.role_repository import RoleRepository
from backend.models.access_control.role_model import Role
from backend.models.authentication.user_model import User
from backend.repositories.authentication.user_repository import UserRepository

class RoleService:
    @staticmethod
    def create_role(name: str, description: str = None) -> Role:
        role = Role(name, description)
        RoleRepository.save(role)
        return role

    @staticmethod
    def assign_role_to_user(user_id: int, role_id: int) -> None:
        user = UserRepository.find_by_id(user_id)
        role = RoleRepository.find_by_id(role_id)
        if user and role:
            user.roles.append(role)
            UserRepository.save(user)

    @staticmethod
    def get_all_roles() -> list[Role]:
        return RoleRepository.find_all()


# File 6: Role Form to Capture Role Data in forms/role_form.py