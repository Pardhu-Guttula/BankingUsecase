# Epic Title: Role-based Access Control

from backend.models.access_control.role_model import Role
from backend.app import db

class RoleRepository:
    @staticmethod
    def save(role: Role) -> None:
        db.session.add(role)
        db.session.commit()

    @staticmethod
    def get_all_roles() -> list[Role]:
        return Role.query.all()

    @staticmethod
    def get_role_by_name(role_name: str) -> Role:
        return Role.query.filter_by(name=role_name).first()

    @staticmethod
    def delete(role: Role) -> None:
        db.session.delete(role)
        db.session.commit()


# File 4: UserRole Repository for User-Role Association in access_control/roles/user_role_repository.py