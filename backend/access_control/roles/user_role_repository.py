# Epic Title: Role-based Access Control

from backend.models.access_control.user_role_model import UserRole
from backend.app import db

class UserRoleRepository:
    @staticmethod
    def assign_role_to_user(user_id: int, role_id: int) -> None:
        user_role = UserRole(user_id=user_id, role_id=role_id)
        db.session.add(user_role)
        db.session.commit()

    @staticmethod
    def remove_role_from_user(user_id: int, role_id: int) -> None:
        user_role = UserRole.query.filter_by(user_id=user_id, role_id=role_id).first()
        if user_role:
            db.session.delete(user_role)
            db.session.commit()


# File 5: Role Service for Business Logic in access_control/services/role_service.py