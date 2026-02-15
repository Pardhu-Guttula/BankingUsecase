# Epic Title: User Authentication and Security

import pyotp
import bcrypt
from backend.models.authentication.user_authentication_model import UserAuthentication
from backend.repositories.authentication.user_authentication_repository import UserAuthenticationRepository

class AuthenticationService:
    @staticmethod
    def hash_password(password: str) -> str:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    @staticmethod
    def verify_password(password: str, password_hash: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))

    @staticmethod
    def generate_mfa_secret() -> str:
        return pyotp.random_base32()

    @staticmethod
    def verify_mfa_token(secret: str, token: str) -> bool:
        totp = pyotp.TOTP(secret)
        return totp.verify(token)

    @staticmethod
    def register_mfa(user_id: int) -> str:
        mfa_secret = AuthenticationService.generate_mfa_secret()
        user_authentication = UserAuthenticationRepository.get_by_user_id(user_id)
        if user_authentication:
            user_authentication.mfa_secret = mfa_secret
            UserAuthenticationRepository.save(user_authentication)
        return mfa_secret

    @staticmethod
    def authenticate_user(user_id: int, password: str, token: str) -> bool:
        user_authentication = UserAuthenticationRepository.get_by_user_id(user_id)
        if user_authentication and AuthenticationService.verify_password(password, user_authentication.password_hash):
            if user_authentication.mfa_secret and AuthenticationService.verify_mfa_token(user_authentication.mfa_secret, token):
                return True
        return False

# File 4: Authentication Controller in controllers/authentication/authentication_controller.py