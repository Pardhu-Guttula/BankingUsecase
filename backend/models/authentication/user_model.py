# Epic Title: User Authentication and Security

from sqlalchemy import Column, Integer, String, Boolean
from backend.app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    is_2fa_enabled = Column(Boolean, default=False)

    def __init__(self, username: str, password: str, email: str, is_2fa_enabled: bool = False):
        self.username = username
        self.password_hash = self._generate_password_hash(password)
        self.email = email
        self.is_2fa_enabled = is_2fa_enabled

    @staticmethod
    def _generate_password_hash(password: str) -> str:
        return generate_password_hash(password)

    def verify_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)


# File 2: User Repository Handling Secure Storage of Credentials in authentication/repositories/user_repository.py