# Epic Title: User Authentication and Security

from backend.authentication.repositories.user_repository import UserRepository
from backend.authentication.repositories.two_factor_repository import TwoFactorAuthRepository
from backend.models.authentication.two_factor_model import TwoFactorAuth
from pyotp import TOTP
from flask import current_app
import base64

class AuthenticationService:
    @staticmethod
    def authenticate(username: str, password: str) -> bool:
        user = UserRepository.get_user_by_username(username)
        if user and UserRepository.verify_password(user, password):
            if user.is_2fa_enabled:
                return False  # Prompt for 2FA
            return True
        return False

    @staticmethod
    def verify_2fa(user_id: int, otp: str) -> bool:
        two_factor = TwoFactorAuthRepository.get_by_user_id(user_id)
        if two_factor:
            totp = TOTP(two_factor.otp_secret)
            return totp.verify(otp)
        return False

    @staticmethod
    def enable_2fa(user_id: int) -> None:
        secret = base64.b32encode(current_app.secret_key.encode()).decode('utf-8')
        two_factor = TwoFactorAuth(user_id=user_id, otp_secret=secret)
        TwoFactorAuthRepository.save(two_factor)


# File 6: Authentication Controller to Handle Login Endpoints in authentication/controllers/authentication_controller.py