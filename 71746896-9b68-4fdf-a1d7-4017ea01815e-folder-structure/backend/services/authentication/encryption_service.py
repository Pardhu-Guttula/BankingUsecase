# Epic Title: Secure User Data

from cryptography.fernet import Fernet
from django.conf import settings

class EncryptionService:
    @staticmethod
    def generate_key() -> bytes:
        # Epic Title: Secure User Data
        return Fernet.generate_key()

    @staticmethod
    def encrypt(data: str, key: bytes) -> str:
        # Epic Title: Secure User Data
        f = Fernet(key)
        return f.encrypt(data.encode()).decode()

    @staticmethod
    def decrypt(token: str, key: bytes) -> str:
        # Epic Title: Secure User Data
        f = Fernet(key)
        return f.decrypt(token.encode()).decode()