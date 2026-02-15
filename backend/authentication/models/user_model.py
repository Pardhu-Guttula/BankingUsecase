# Epic Title: Secure User Data

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from cryptography.fernet import Fernet

db = SQLAlchemy()
ENCRYPTION_KEY = b'YOUR_SECRET_ENCRYPTION_KEY'  # Should be replaced with a secure key

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    encrypted_data = db.Column(db.LargeBinary, nullable=True)

    def set_password(self, password: str) -> None:
        # Epic Title: Secure User Data
        self.password = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        # Epic Title: Secure User Data
        return check_password_hash(self.password, password)

    def encrypt_data(self, data: str) -> None:
        # Epic Title: Secure User Data
        cipher = Fernet(ENCRYPTION_KEY)
        self.encrypted_data = cipher.encrypt(data.encode())

    def decrypt_data(self) -> str:
        # Epic Title: Secure User Data
        cipher = Fernet(ENCRYPTION_KEY)
        return cipher.decrypt(self.encrypted_data).decode() if self.encrypted_data else None