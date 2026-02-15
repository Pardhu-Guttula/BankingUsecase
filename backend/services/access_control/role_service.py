# Epic Title: Role-based Access Control

from backend.repositories.access_control.role_repository import RoleRepository
from backend.models.access_control.role_model import Role

class RoleService:
    @staticmethod
    def create_role(name: str, description: str = '') -> Role:
        role = Role(name=name, description=description)
        RoleRepository.save(role)
        return role

    @staticmethod
    def update_role(role_id: int, name: str = None, description: str = None) -> Role:
        role = RoleRepository.get_role_by_id(role_id)
        if name is not None:
            role.name = name
        if description is not None:
            role.description = description
        RoleRepository.update(role)
        return role

    @staticmethod
    def delete_role(role_id: int) -> None:
        role = RoleRepository.get_role_by_id(role_id)
        RoleRepository.delete(role)

    @staticmethod
    def assign_role_to_user(user, role_id: int) -> None:
        role = RoleRepository.get_role_by_id(role_id)
        user.role = role
        db.session.commit()

    @staticmethod
    def remove_role_from_user(user) -> None:
        user.role = None
        db.session.commit()


# File 5: Role Controller in access_control/controllers/role_controller.py