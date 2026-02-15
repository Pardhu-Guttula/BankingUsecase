# Epic Title: User Authentication and Security

from backend.models.authentication.user_security_model import UserSecurity
from backend.app import db

class UserSecurityRepository:
    @staticmethod
    def get_by_user_id(user_id: int) -> UserSecurity:
        return UserSecurity.query.filter_by(user_id=user_id).first()

    @staticmethod
    def save(user_security: UserSecurity) -> None:
        db.session.add(user_security)
        db.session.commit()

    @staticmethod
    def update(user_security: UserSecurity) -> None:
        db.session.commit()


# File 4: User Authentication Service Layer in services/authentication/user_authentication_service.py