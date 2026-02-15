# Epic Title: Define User Roles

from backend.accesscontrol.models.user_role_model import UserRole
from backend.app import db

class UserRoleRepository:
    @staticmethod
    def save(user_role: UserRole) -> None:
        db.session.add(user_role)
        db.session.commit()

    @staticmethod
    def get_by_user_id(user_id: int) -> list[UserRole]:
        return UserRole.query.filter_by(user_id=user_id).all()


# File 5: Role Service for Business Logic in accesscontrol/services/role_service.py