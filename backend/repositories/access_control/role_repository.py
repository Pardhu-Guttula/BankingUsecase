# Epic Title: Define User Roles

from backend.models.access_control.role_model import Role
from backend.app import db

class RoleRepository:
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

    @staticmethod
    def find_by_id(role_id: int) -> Role:
        return Role.query.filter_by(id=role_id).first()

    @staticmethod
    def find_all() -> list[Role]:
        return Role.query.all()


# File 3: Role Service in `services/access_control/role_service.py`