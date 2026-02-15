# Epic Title: User Authentication and Security

from backend.models.authentication.user_model import User
from backend.app import db

class UserRepository:
    @staticmethod
    def get_user_by_username(username: str) -> User:
        return User.query.filter_by(username=username).first()

    @staticmethod
    def verify_password(user: User, password: str) -> bool:
        return user.verify_password(password)

    @staticmethod
    def save(user: User) -> None:
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def create_user(username: str, password: str, email: str) -> User:
        new_user = User(username=username, password=password, email=email)
        UserRepository.save(new_user)
        return new_user


# File 3: Authentication Controller to Handle Registration Endpoint in authentication/controllers/authentication_controller.py