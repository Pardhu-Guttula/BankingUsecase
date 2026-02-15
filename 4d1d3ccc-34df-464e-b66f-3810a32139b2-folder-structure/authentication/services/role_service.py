# Epic Title: Role-based Access Control

from authentication.repositories.role_repository import RoleRepository
from authentication.models.role_model import Role

class RoleService:
    @staticmethod
    def define_role(name: str, description: str = None) -> Role:
        role = Role(name, description)
        RoleRepository.save(role)
        return role

    @staticmethod
    def assign_role(user_id: int, role_id: int) -> None:
        user = User.query.get(user_id)
        user.role_id = role_id
        db.session.commit()

    @staticmethod
    def get_all_roles() -> list[Role]:
        return RoleRepository.get_all()


# File 5: Role Controller for Handling Requests in authentication/controllers/role_controller.py