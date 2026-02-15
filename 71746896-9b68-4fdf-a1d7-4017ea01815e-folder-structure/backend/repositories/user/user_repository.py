# Epic Title: Display Tailored Products

from django.contrib.auth.models import User
from typing import Dict, Any, Optional

class UserRepository:
    @staticmethod
    def get_user_by_username(username: str) -> Optional[User]:
        # Epic Title: Display Tailored Products
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

    @staticmethod
    def get_profile(user: User) -> Dict[str, Any]:
        # Epic Title: Display Tailored Products
        # Mock profile for the sake of example
        return {
            'credit_score': 720,
            'income': 60000,
            'age': 30
        }

    @staticmethod
    def set_profile(user: User, profile: Dict[str, Any]) -> None:
        # Epic Title: Display Tailored Products
        # In reality, this would save to a database
        pass