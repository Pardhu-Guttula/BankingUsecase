# Epic Title: Implement Secure Login Mechanism

from authentication.repositories.user_repository import UserRepository
from authentication.services.two_factor_service import TwoFactorService
from werkzeug.security import check_password_hash
from flask_login import login_user
from typing import Optional

class AuthenticationService:
    @staticmethod
    def authenticate(username: str, password: str) -> Optional[int]:
        user = UserRepository.get_by_username(username)
        if user and check_password_hash(user.password_hash, password):
            if user.two_factor_enabled:
                code = TwoFactorService.generate_two_factor_code(user.id)
                # Send code via SMS or email here
                return user.id  # Return user id for further verification
            login_user(user)
            return None
        return None

    @staticmethod
    def verify_two_factor(user_id: int, code: str) -> bool:
        if TwoFactorService.verify_two_factor_code(user_id, code):
            user = UserRepository.get_by_id(user_id)
            login_user(user)
            return True
        return False


# File 7: User Authentication Controller in authentication/controllers/authentication_controller.py