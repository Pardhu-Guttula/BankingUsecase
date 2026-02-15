# Epic Title: User Authentication and Security

from backend.models.authentication.user_model import User
import pyotp
from backend.repositories.authentication.user_repository import UserRepository

class AuthenticationService:
    @staticmethod
    def validate_user_credentials(username: str, password: str) -> User:
        user = UserRepository.get_user_by_username(username)
        if user and user.verify_password(password):
            return user
        return None

    @staticmethod
    def generate_mfa_secret() -> str:
        return pyotp.random_base32()

    @staticmethod
    def validate_mfa_token(user: User, token: str) -> bool:
        totp = pyotp.TOTP(user.mfa_secret)
        return totp.verify(token)


# File 3: User Repository for User Info Access in repositories/authentication/user_repository.py