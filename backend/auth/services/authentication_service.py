# Epic Title: User Authentication and Security

import pyotp
from flask_login import login_user
from backend.auth.repositories.user_repository import UserRepository
from backend.models.authentication.user_model import User

class AuthenticationService:
    @staticmethod
    def verify_password(user: User, password: str) -> bool:
        return user.verify_password(password)

    @staticmethod
    def generate_mfa_secret() -> str:
        return pyotp.random_base32()

    @staticmethod
    def verify_mfa_token(user: User, token: str) -> bool:
        if user.mfa_secret:
            totp = pyotp.TOTP(user.mfa_secret)
            return totp.verify(token)
        return False

    @staticmethod
    def login_with_mfa(username: str, password: str, token: str) -> bool:
        user = UserRepository.find_by_username(username)
        if user and AuthenticationService.verify_password(user, password):
            if user.mfa_enabled:
                if AuthenticationService.verify_mfa_token(user, token):
                    login_user(user)
                    return True
            else:
                login_user(user)
                return True
        return False


# File 4: MFA Form for Login in forms/mfa_form.py