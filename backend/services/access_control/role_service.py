# Epic Title: Define User Roles

from backend.repositories.access_control.role_repository import RoleRepository
from backend.models.access_control.role_model import Role

class RoleService:
    @staticmethod
    def create_role(name: str, description: str = None) -> Role:
        role = Role(name=name, description=description)
        RoleRepository.save(role)
        return role

    @staticmethod
    def update_role(role_id: int, name: str, description: str = None) -> Role:
        role = RoleRepository.find_by_id(role_id)
        if role:
            role.name = name
            role.description = description
            RoleRepository.update(role)
        return role

    @staticmethod
    def delete_role(role_id: int) -> None:
        role = RoleRepository.find_by_id(role_id)
        if role:
            RoleRepository.delete(role)

    @staticmethod
    def get_role(role_id: int) -> Role:
        return RoleRepository.find_by_id(role_id)

    @staticmethod
    def get_all_roles() -> list[Role]:
        return RoleRepository.find_all()


# File 4: Role Controller in `controllers/access_control/role_controller.py`