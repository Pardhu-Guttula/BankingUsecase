# Epic Title: Role-based Access Control

from backend.models.access_control.role_model import Role
from backend.models.access_control.permission_model import Permission
from backend.models.access_control.role_permission_association import role_permissions
from backend.repositories.access_control.role_repository import RoleRepository
from backend.repositories.access_control.permission_repository import PermissionRepository
from backend.app import db

class RoleService:
    @staticmethod
    def create_role(name: str, description: str) -> Role:
        role = Role(name=name, description=description)
        RoleRepository.save(role)
        return role

    @staticmethod
    def get_all_roles() -> list[Role]:
        return RoleRepository.find_all()

    @staticmethod
    def assign_permissions(role_name: str, permission_names: list[str]) -> Role:
        role = RoleRepository.find_by_name(role_name)
        if not role:
            return None

        permissions = Permission.query.filter(Permission.name.in_(permission_names)).all()
        role.permissions = permissions
        db.session.commit()
        return role

# File 5: Role Controller Updated for Permission Assignment in controllers/access_control/role_controller.py (Modified)