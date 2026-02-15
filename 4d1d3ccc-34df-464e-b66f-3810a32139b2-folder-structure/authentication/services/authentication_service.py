# Epic Title: Manage Secure Storage of Credentials

from authentication.repositories.user_repository import UserRepository
from werkzeug.security import generate_password_hash
from flask_login import login_user
from typing import Optional

class AuthenticationService:
    @staticmethod
    def authenticate(username: str, password: str) -> Optional[User]:
        user = UserRepository.get_by_username(username)
        if user and user.check_password(password):
            login_user(user)
            return user
        return None

    @staticmethod
    def register(username: str, password: str, email: str, phone_number: str, two_factor_enabled: bool) -> User:
        user = User(
            username=username,
            password=generate_password_hash(password),  # Hash password
            email=email,
            phone_number=phone_number,
            two_factor_enabled=two_factor_enabled
        )
        UserRepository.save(user)
        return user


# File 5: User Authentication Controller in authentication/controllers/authentication_controller.py