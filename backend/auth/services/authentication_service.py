# Epic Title: User Authentication and Security

import pyotp
from flask_login import login_user, logout_user, current_user
from datetime import datetime, timedelta
from backend.auth.repositories.user_repository import UserRepository
from backend.models.authentication.user_model import User
from cryptography.fernet import Fernet

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
            decrypted_mfa_secret = user.decrypt_mfa_secret()
            totp = pyotp.TOTP(decrypted_mfa_secret)
            return totp.verify(token)
        return False

    @staticmethod
    def login_with_mfa(username: str, password: str, token: str) -> bool:
        user = UserRepository.find_by_username(username)
        if user and AuthenticationService.verify_password(user, password):
            if user.mfa_enabled:
                if AuthenticationService.verify_mfa_token(user, token):
                    login_user(user)
                    UserRepository.update_last_activity(user)
                    return True
            else:
                login_user(user)
                UserRepository.update_last_activity(user)
                return True
        return False

    @staticmethod
    def check_session_expiry(timeout: int = 15) -> bool:
        if current_user.is_authenticated:
            if UserRepository.is_session_expired(current_user, timeout):
                logout_user()
                return True
            else:
                UserRepository.update_last_activity(current_user)
        return False


# File 4: Update Main App to Include Encryption Key Setup in app.py