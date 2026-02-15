# Epic Title: User Authentication and Security

from typing import Optional
import pyotp
from backend.repositories.authentication.user_security_repository import UserSecurityRepository
from backend.models.authentication.user_security_model import UserSecurity
from backend.models.authentication.user_model import User
from flask_login import login_user

class UserAuthenticationService:
    @staticmethod
    def verify_password(user: User, password: str) -> bool:
        return user.verify_password(password)

    @staticmethod
    def set_up_2fa(user_id: int) -> str:
        secret = pyotp.random_base32()
        user_security = UserSecurityRepository.get_by_user_id(user_id)
        if user_security:
            user_security.otp_secret = secret
        else:
            user_security = UserSecurity(user_id=user_id, otp_secret=secret)
            UserSecurityRepository.save(user_security)
        return secret

    @staticmethod
    def verify_otp(user_id: int, otp: str) -> bool:
        user_security = UserSecurityRepository.get_by_user_id(user_id)
        if user_security and user_security.is_otp_enabled:
            totp = pyotp.TOTP(user_security.otp_secret)
            return totp.verify(otp)
        return False

    @staticmethod
    def login(user: User, password: str, otp: Optional[str] = None) -> bool:
        if not UserAuthenticationService.verify_password(user, password):
            return False
        if user.is_2fa_enabled:
            if not otp or not UserAuthenticationService.verify_otp(user.id, otp):
                return False
        login_user(user)
        return True


# File 5: Authentication Controller to Handle Login and 2FA in authentication/controllers/authentication_controller.py