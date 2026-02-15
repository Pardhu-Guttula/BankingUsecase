# Epic Title: Role-Based Access Control

from django.contrib.auth.models import User
from typing import Optional

class UserRepository:
    def get_user_by_username(self, username: str) -> Optional[User]:
        # Epic Title: Role-Based Access Control
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None