# Epic Title: User Authentication and Security

from backend.models.authentication.user_model import User
from backend.app import db

class UserRepository:
    @staticmethod
    def get_user_by_username(username: str) -> User:
        return User.query.filter_by(username=username).first()


# File 4: Authentication Controller Handling Login Process with MFA in authentication/controllers/authentication_controller.py