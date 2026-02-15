# Epic Title: Display Tailored Products

from django.contrib.auth.models import User
from typing import Optional, Dict

class UserRepository:
    @staticmethod
    def get_user_by_username(username: str) -> Optional[User]:
        # Epic Title: Display Tailored Products
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

    @staticmethod
    def get_profile(user: User) -> Dict[str, str]:
        # Epic Title: Display Tailored Products
        # Mock profile for the sake of example
        return {'username': user.username, 'tags': ['High Net-Worth Individuals', 'Salaried Employees']}