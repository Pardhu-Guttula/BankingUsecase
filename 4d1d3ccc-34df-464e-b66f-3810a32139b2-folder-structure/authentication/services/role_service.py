# Epic Title: Role-based Access Control

from authentication.repositories.role_repository import RoleRepository
from authentication.models.role_model import Role
from authentication.models.permission_model import Permission
from backend.app import db

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

    @staticmethod
    def assign_permission_to_role(role_id: int, permission_id: int) -> None:
        role = Role.query.get(role_id)
        permission = Permission.query.get(permission_id)
        role.permissions.append(permission)
        db.session.commit()


# File 7: Permission Service for Business Logic in authentication/services/permission_service.py