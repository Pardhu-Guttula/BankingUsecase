# Epic Title: User Authentication and Security

from backend.models.authentication.user_model import User
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
    def get_by_email(email: str) -> User:
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_by_id(user_id: int) -> User:
        return User.query.filter_by(id=user_id).first()

# File 3: User Service in services/authentication/user_service.py