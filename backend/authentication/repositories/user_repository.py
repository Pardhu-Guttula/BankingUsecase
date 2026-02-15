# Epic Title: Secure User Data

from typing import Optional
from werkzeug.security import generate_password_hash, check_password_hash
from backend.authentication.models.user_model import User

class UserRepository:
    @staticmethod
    def find_by_email(email: str) -> Optional[User]:
        # Epic Title: Secure User Data
        # Replace this with actual database query
        return User.query.filter_by(email=email).first()

    @staticmethod
    def find_by_id(user_id: int) -> Optional[User]:
        # Epic Title: Secure User Data
        # Replace this with actual database query
        return User.query.get(user_id)

    @staticmethod
    def add_user(email: str, password: str, mobile: str):
        # Epic Title: Secure User Data
        hashed_password = generate_password_hash(password)
        encrypted_mobile = EncryptionService.encrypt(mobile)
        new_user = User(email=email, password=hashed_password, mobile=encrypted_mobile)
        new_user.save()