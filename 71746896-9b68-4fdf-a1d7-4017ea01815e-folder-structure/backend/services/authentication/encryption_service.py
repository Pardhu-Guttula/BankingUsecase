# Epic Title: Secure User Data

import hashlib
import base64
import os
from cryptography.fernet import Fernet

class EncryptionService:
    @staticmethod
    def hash_password(password: str) -> str:
        # Epic Title: Secure User Data
        salt = os.urandom(16)
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        return base64.b64encode(salt + hashed_password).decode('utf-8')

    @staticmethod
    def encrypt_data(data: str) -> str:
        # Epic Title: Secure User Data
        key = Fernet.generate_key()
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data.encode())
        return base64.b64encode(key + encrypted_data).decode('utf-8')

    @staticmethod
    def decrypt_data(encrypted_data: str) -> str:
        # Epic Title: Secure User Data
        encrypted_data_bytes = base64.b64decode(encrypted_data.encode('utf-8'))
        key = encrypted_data_bytes[:32]
        data = encrypted_data_bytes[32:]
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(data).decode('utf-8')
        return decrypted_data