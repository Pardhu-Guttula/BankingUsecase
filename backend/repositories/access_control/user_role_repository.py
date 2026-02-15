# Epic Title: Role-based Access Control

from backend.models.access_control.user_role_model import UserRole
from backend.app import db

class UserRoleRepository:
    @staticmethod
    def save(user_role: UserRole) -> None:
        db.session.add(user_role)
        db.session.commit()

    @staticmethod
    def get_roles_by_user(user_id: int) -> list[UserRole]:
        return UserRole.query.filter_by(user_id=user_id).all()

# File 5: Role Management Service in services/access_control/role_service.py