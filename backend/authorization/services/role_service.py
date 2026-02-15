# Epic Title: Role-Based Access Control

from typing import List
from backend.authorization.models.user_model import User
from backend.authorization.repositories.role_repository import RoleRepository

class RoleService:
    @staticmethod
    def assign_role(user: User, role: str):
        # Epic Title: Role-Based Access Control
        RoleRepository.assign_role_to_user(user, role)

    @staticmethod
    def has_role(user: User, role: str) -> bool:
        # Epic Title: Role-Based Access Control
        return RoleRepository.user_has_role(user, role)