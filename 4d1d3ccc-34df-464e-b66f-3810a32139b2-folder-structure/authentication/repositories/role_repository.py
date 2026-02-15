# Epic Title: Role-based Access Control

from authentication.models.role_model import Role
from backend.app import db

class RoleRepository:
    @staticmethod
    def save(role: Role) -> None:
        db.session.add(role)
        db.session.commit()

    @staticmethod
    def get_all() -> list[Role]:
        return Role.query.all()

    @staticmethod
    def get_by_id(role_id: int) -> Role:
        return Role.query.get(role_id)


# File 4: Role Service for Business Logic in authentication/services/role_service.py