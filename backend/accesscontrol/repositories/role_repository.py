# Epic Title: Define User Roles

from backend.accesscontrol.models.role_model import Role
from backend.app import db

class RoleRepository:
    @staticmethod
    def save(role: Role) -> None:
        db.session.add(role)
        db.session.commit()

    @staticmethod
    def get_by_id(role_id: int) -> Role:
        return Role.query.get(role_id)

    @staticmethod
    def get_all() -> list[Role]:
        return Role.query.all()


# File 4: UserRole Repository for Database Operations in accesscontrol/repositories/user_role_repository.py