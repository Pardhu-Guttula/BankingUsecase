# Epic Title: User Authentication and Authorization

from cryptography.fernet import Fernet
import base64

class EncryptionService:
    # Epic Title: Secure User Data
    key = base64.urlsafe_b64encode(Fernet.generate_key())  # Key should be stored securely
    cipher_suite = Fernet(key)

    @staticmethod
    def encrypt(data: str) -> str:
        # Epic Title: Secure User Data
        return EncryptionService.cipher_suite.encrypt(data.encode()).decode()

    @staticmethod
    def decrypt(data: str) -> str:
        # Epic Title: Secure User Data
        return EncryptionService.cipher_suite.decrypt(data.encode()).decode()
