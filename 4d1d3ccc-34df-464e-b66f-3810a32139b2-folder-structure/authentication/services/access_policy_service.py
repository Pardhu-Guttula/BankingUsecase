# Epic Title: Role-based Access Control

from flask_login import current_user
from sqlalchemy.orm import scoped_session, sessionmaker
from typing import List
from backend.app import db
from authentication.models.permission_model import Permission
from authentication.models.role_model import Role

class AccessPolicyService:
    @staticmethod
    def has_permission(permission_name: str) -> bool:
        if not current_user.is_authenticated:
            return False
        
        user_role = current_user.role
        if not user_role:
            return False

        session = scoped_session(sessionmaker(bind=db))
        permission = session.query(Permission).filter_by(name=permission_name).first()
        session.remove()

        return permission in user_role.permissions

    @staticmethod
    def get_allowed_services() -> List[str]:
        if not current_user.is_authenticated:
            return []

        user_role = current_user.role
        if not user_role:
            return []

        allowed_services = [permission.name for permission in user_role.permissions]
        return allowed_services


# File 2: Access Policy Decorator for Role-based Restrictions in authentication/decorators/access_policy_decorator.py