# Epic Title: Role-Based Access Control

from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class RoleService:
    @staticmethod
    def assign_role(user_id: int, role: str) -> None:
        # Epic Title: Role-Based Access Control
        user = User.objects.get(id=user_id)
        group, created = Group.objects.get_or_create(name=role)
        user.groups.add(group)
        user.save()

    @staticmethod
    def get_all_roles() -> list:
        # Epic Title: Role-Based Access Control
        return list(Group.objects.values_list('name', flat=True))

    @staticmethod
    def user_has_role(user: User, role: str) -> bool:
        # Epic Title: Role-Based Access Control
        return user.groups.filter(name=role).exists()