# Epic Title: Implement Multi-Factor Authentication

from django.contrib.auth.models import User
from typing import Optional

class UserRepository:
    def get_user_by_username(self, username: str) -> Optional[User]:
        # Epic Title: Implement Multi-Factor Authentication
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None