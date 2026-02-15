# Epic Title: Role-based Access Control

from backend.models.access_control.role_model import Role
from backend.app import db

class RoleRepository:
    @staticmethod
    def save(role: Role) -> None:
        db.session.add(role)
        db.session.commit()

    @staticmethod
    def find_by_id(role_id: int) -> Role:
        return Role.query.get(role_id)

    @staticmethod
    def find_by_name(name: str) -> Role:
        return Role.query.filter_by(name=name).first()

    @staticmethod
    def find_all() -> list[Role]:
        return Role.query.all()


# File 4: User Repository to Manage User Role Assignments in repositories/authentication/user_repository.py