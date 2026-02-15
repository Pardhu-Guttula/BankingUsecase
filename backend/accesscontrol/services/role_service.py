# Epic Title: Define User Roles

from backend.accesscontrol.repositories.role_repository import RoleRepository
from backend.accesscontrol.repositories.user_role_repository import UserRoleRepository
from backend.accesscontrol.models.role_model import Role
from backend.accesscontrol.models.user_role_model import UserRole

class RoleService:
    @staticmethod
    def create_role(name: str) -> Role:
        role = Role(name=name)
        RoleRepository.save(role)
        return role

    @staticmethod
    def assign_role_to_user(user_id: int, role_id: int) -> None:
        user_role = UserRole(user_id=user_id, role_id=role_id)
        UserRoleRepository.save(user_role)

    @staticmethod
    def get_all_roles() -> list[Role]:
        return RoleRepository.get_all()

    @staticmethod
    def get_roles_for_user(user_id: int) -> list[UserRole]:
        return UserRoleRepository.get_by_user_id(user_id)


# File 6: Role Controller for Handling Requests in accesscontrol/controllers/role_controller.py