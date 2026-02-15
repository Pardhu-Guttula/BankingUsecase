# Epic Title: Role-Based Access Control

from django.contrib.auth.models import User

class RoleService:
    @staticmethod
    def assign_role(user: User, role: str) -> None:
        # Epic Title: Role-Based Access Control
        user.profile.roles.add(role)
        user.save()

    @staticmethod
    def remove_role(user: User, role: str) -> None:
        # Epic Title: Role-Based Access Control
        user.profile.roles.remove(role)
        user.save()

    @staticmethod
    def has_role(user: User, role: str) -> bool:
        # Epic Title: Role-Based Access Control
        return role in user.profile.roles.all()