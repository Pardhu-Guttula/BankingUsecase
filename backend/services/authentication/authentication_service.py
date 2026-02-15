# Epic Title: User Authentication and Security

from flask_login import current_user, login_user, logout_user
from backend.repositories.authentication.user_repository import UserRepository
from backend.app import db
from werkzeug.security import check_password_hash, generate_password_hash
import pyotp

class AuthenticationService:
    @staticmethod
    def authenticate(username: str, password: str) -> bool:
        user = UserRepository.find_by_username(username)
        if user and check_password_hash(user.password, password):
            if user.mfa_enabled:
                return "mfa_required"
            login_user(user)
            return True
        return False

    @staticmethod
    def verify_mfa(username: str, token: str) -> bool:
        user = UserRepository.find_by_username(username)
        if user and user.mfa_enabled:
            totp = pyotp.TOTP(user.mfa_secret)
            if totp.verify(token):
                login_user(user)
                return True
        return False

    @staticmethod
    def setup_mfa(user_id: int):
        user = UserRepository.find_by_id(user_id)
        if user:
            secret = pyotp.random_base32()
            user.mfa_secret = secret
            user.mfa_enabled = True
            db.session.commit()
            return secret
        return None

    @staticmethod
    def disable_mfa(user_id: int):
        user = UserRepository.find_by_id(user_id)
        if user:
            user.mfa_secret = None
            user.mfa_enabled = False
            db.session.commit()


# File 3: User Repository for Database Operations in repositories/authentication/user_repository.py