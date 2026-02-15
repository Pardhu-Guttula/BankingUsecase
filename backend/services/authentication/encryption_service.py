# Epic Title: User Authentication and Security

from werkzeug.security import generate_password_hash, check_password_hash
from cryptography.fernet import Fernet

class EncryptionService:
    @staticmethod
    def generate_key() -> bytes:
        return Fernet.generate_key()

    @staticmethod
    def encrypt_password(password: str) -> str:
        return generate_password_hash(password)

    @staticmethod
    def verify_password(stored_password: str, provided_password: str) -> bool:
        return check_password_hash(stored_password, provided_password)

    @staticmethod
    def encrypt_data(key: bytes, data: str) -> bytes:
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data.encode())
        return encrypted_data

    @staticmethod
    def decrypt_data(key: bytes, encrypted_data: bytes) -> str:
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data).decode()
        return decrypted_data


# File 2: Update User Model to Include Session Key Encryption in models/authentication/user_model.py