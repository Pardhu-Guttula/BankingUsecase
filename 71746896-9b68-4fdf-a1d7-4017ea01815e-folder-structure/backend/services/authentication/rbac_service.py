# Epic Title: Role-Based Access Control

from django.contrib.auth.models import User, Group
from typing import Optional

class RBACService:
    @staticmethod
    def assign_role(username: str, role_name: str) -> bool:
        # Epic Title: Role-Based Access Control
        try:
            user = User.objects.get(username=username)
            role, _ = Group.objects.get_or_create(name=role_name)
            user.groups.add(role)
            return True
        except User.DoesNotExist:
            return False

    @staticmethod
    def has_access(user: User, resource: str) -> bool:
        # Epic Title: Role-Based Access Control
        # Simplified resource checking logic for example purposes
        return user.groups.filter(name=resource).exists()