# Epic Title: Implement Multi-Factor Authentication

from typing import Optional
from backend.authentication.models.user_model import User

class UserRepository:
    @staticmethod
    def find_by_email(email: str) -> Optional[User]:
        # Epic Title: Implement Multi-Factor Authentication
        # Replace this with actual database query
        return User.query.filter_by(email=email).first()

    @staticmethod
    def find_by_id(user_id: int) -> Optional[User]:
        # Epic Title: Implement Multi-Factor Authentication
        # Replace this with actual database query
        return User.query.get(user_id)