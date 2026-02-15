# Epic Title: User Authentication and Security

from backend.models.authentication.user_model import User
from backend.repositories.authentication.user_repository import UserRepository


class UserService:
    @staticmethod
    def create_user(username: str, email: str, password: str) -> User:
        user = User(username=username, email=email, password=password)
        UserRepository.save(user)
        return user

    @staticmethod
    def authenticate(username: str, password: str) -> User:
        user = UserRepository.get_user_by_username(username)
        if user and user.verify_password(password):
            return user
        return None

    @staticmethod
    def get_user_by_id(user_id: int) -> User:
        return UserRepository.get_user_by_id(user_id)


# File 4: Authentication Controller to Handle User Registration and Login in authentication/controllers/authentication_controller.py