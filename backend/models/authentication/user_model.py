# Epic Title: Manage Secure Storage of Credentials

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from backend.app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(150), unique=True, nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    mfa_secret = Column(String(32), nullable=False)

    def __init__(self, username: str, email: str, password: str):
        self.username = User.encrypt(username)
        self.email = User.encrypt(email)
        self.password_hash = generate_password_hash(password)
        self.is_active = True
        self.created_at = datetime.utcnow()
        self.mfa_secret = MFAService.generate_secret()

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)
    
    @staticmethod
    def encrypt(data: str) -> str:
        key = os.environ.get('ENCRYPTION_KEY').encode()
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(data.encode()) + encryptor.finalize()
        return base64.b64encode(iv + ciphertext).decode('utf-8')
    
    @staticmethod
    def decrypt(encrypted_data: str) -> str:
        key = os.environ.get('ENCRYPTION_KEY').encode()
        data = base64.b64decode(encrypted_data)
        iv = data[:16]
        ciphertext = data[16:]
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        return decryptor.update(ciphertext) + decryptor.finalize()


# File 2: Encryption Service in services/authentication/encryption_service.py