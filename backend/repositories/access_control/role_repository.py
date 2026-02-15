# Epic Title: Role-based Access Control

from backend.models.access_control.role_model import Role
from backend.app import db

class RoleRepository:
    @staticmethod
    def get_all_roles() -> list[Role]:
        return Role.query.all()

    @staticmethod
    def get_role_by_id(role_id: int) -> Role:
        return Role.query.get(role_id)

    @staticmethod
    def save(role: Role) -> None:
        db.session.add(role)
        db.session.commit()

    @staticmethod
    def update(role: Role) -> None:
        db.session.commit()

    @staticmethod
    def delete(role: Role) -> None:
        db.session.delete(role)
        db.session.commit()


# File 4: Role Service Layer in services/access_control/role_service.py