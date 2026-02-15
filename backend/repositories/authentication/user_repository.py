# Epic Title: Implement Secure Login Mechanism

from backend.models.authentication.user_model import User
from backend.app import db

class UserRepository:
    @staticmethod
    def save(user: User) -> None:
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def find_by_username(username: str) -> User | None:
        return User.query.filter_by(username=username).first()

    @staticmethod
    def find_by_email(email: str) -> User | None:
        return User.query.filter_by(email=email).first()


# File 3: Multi-Factor Authentication Service in services/authentication/mfa_service.py