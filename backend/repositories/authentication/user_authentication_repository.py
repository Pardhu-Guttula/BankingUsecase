# Epic Title: User Authentication and Security

from backend.models.authentication.user_authentication_model import UserAuthentication
from backend.app import db

class UserAuthenticationRepository:
    @staticmethod
    def save(user_authentication: UserAuthentication) -> None:
        db.session.add(user_authentication)
        db.session.commit()

    @staticmethod
    def get_by_user_id(user_id: int) -> UserAuthentication:
        return UserAuthentication.query.filter_by(user_id=user_id).first()

# File 3: Authentication Service in services/authentication/authentication_service.py