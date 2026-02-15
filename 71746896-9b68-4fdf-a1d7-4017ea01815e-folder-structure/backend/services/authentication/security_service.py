# Epic Title: Secure User Data

from cryptography.fernet import Fernet
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from backend.repositories.user.user_repository import UserRepository
import base64

class SecurityService:
    @staticmethod
    def encrypt_user_data(user_id: int) -> None:
        # Epic Title: Secure User Data
        user = User.objects.get(id=user_id)
        user_profile = UserRepository.get_profile(user)

        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        encrypted_data = cipher_suite.encrypt(str(user_profile).encode())
        
        user_profile['encrypted_data'] = base64.urlsafe_b64encode(encrypted_data).decode()
        UserRepository.set_profile(user, user_profile)

    @staticmethod
    def hash_password(password: str) -> str:
        # Epic Title: Secure User Data
        return make_password(password)