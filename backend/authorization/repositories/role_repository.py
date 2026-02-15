# Epic Title: Role-Based Access Control

from backend.authorization.models.role_model import Role
from backend.authorization.models.user_model import User

class RoleRepository:
    @staticmethod
    def assign_role_to_user(user: User, role_name: str):
        # Epic Title: Role-Based Access Control
        role = Role.query.filter_by(name=role_name).first()
        if role and role not in user.roles:
            user.roles.append(role)
            user.save()

    @staticmethod
    def user_has_role(user: User, role_name: str) -> bool:
        # Epic Title: Role-Based Access Control
        role = Role.query.filter_by(name=role_name).first()
        return role in user.roles if role else False