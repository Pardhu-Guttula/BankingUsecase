# Epic Title: Role-based Access Control

from backend.models.access_control.role_model import Role
from backend.repositories.access_control.role_repository import RoleRepository

class RoleService:
    @staticmethod
    def create_role(name: str, description: str) -> Role:
        role = Role(name=name, description=description)
        RoleRepository.save(role)
        return role

    @staticmethod
    def get_all_roles() -> list[Role]:
        return RoleRepository.find_all()

# File 4: Role Controller in controllers/access_control/role_controller.py