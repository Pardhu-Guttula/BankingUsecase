# Epic Title: Role-based Access Control

from backend.models.access_control.role_model import Role
from backend.app import db

class RoleRepository:
    @staticmethod
    def save(role: Role) -> None:
        db.session.add(role)
        db.session.commit()

    @staticmethod
    def find_all() -> list[Role]:
        return Role.query.all()

    @staticmethod
    def find_by_name(name: str) -> Role | None:
        return Role.query.filter_by(name=name).first()

# File 3: Role Service in services/access_control/role_service.py