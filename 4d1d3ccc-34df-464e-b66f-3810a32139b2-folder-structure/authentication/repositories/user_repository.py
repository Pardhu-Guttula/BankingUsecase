# Epic Title: Manage Secure Storage of Credentials

from authentication.models.user_model import User
from backend.app import db

class UserRepository:
    @staticmethod
    def save(user: User) -> None:
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def get_by_username(username: str) -> User:
        return User.query.filter_by(username=username).first()

    @staticmethod
    def get_by_id(user_id: int) -> User:
        return User.query.get(user_id)


# File 4: User Authentication Service in authentication/services/authentication_service.py