# Epic Title: Manage Secure Storage of Credentials

from backend.models.authentication.user_model import User
from backend.app import db
from backend.services.authentication.encryption_service import EncryptionService
import os

encryption_service = EncryptionService(os.environ.get('ENCRYPTION_KEY').encode())

class UserRepository:
    @staticmethod
    def save(user: User) -> None:
        user.username = encryption_service.encrypt(user.username)
        user.email = encryption_service.encrypt(user.email)
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def find_by_username(username: str) -> User | None:
        encrypted_username = encryption_service.encrypt(username)
        return User.query.filter_by(username=encrypted_username).first()

    @staticmethod
    def find_by_email(email: str) -> User | None:
        encrypted_email = encryption_service.encrypt(email)
        return User.query.filter_by(email=encrypted_email).first()


# File 4: Example Usage in Authentication Controller in controllers/authentication/authentication_controller.py