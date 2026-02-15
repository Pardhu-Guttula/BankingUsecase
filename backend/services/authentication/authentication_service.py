# Epic Title: User Authentication and Security

from werkzeug.security import check_password_hash
from flask_login import login_user
import pyotp
from backend.models.authentication.user_model import User
from backend.repositories.authentication.user_repository import UserRepository
from flask import session

class AuthenticationService:
    @staticmethod
    def authenticate(username: str, password: str) -> User:
        user = UserRepository.find_by_username(username)
        if user and user.check_password(password):  # Securely check the password
            session['pre_mfa_user_id'] = user.id
            return user
        return None

    @staticmethod
    def verify_mfa_token(user_id: int, token: str) -> bool:
        user = UserRepository.find_by_id(user_id)
        if user and user.mfa_secret:
            totp = pyotp.TOTP(user.mfa_secret)
            return totp.verify(token)
        return False

    @staticmethod
    def login_user_with_mfa(user_id: int, token: str) -> bool:
        if AuthenticationService.verify_mfa_token(user_id, token):
            user = UserRepository.find_by_id(user_id)
            if user:
                login_user(user)
                session.pop('pre_mfa_user_id', None)
                return True
        return False

# File 4: Authentication Controller in authentication/controllers/authentication_controller.py