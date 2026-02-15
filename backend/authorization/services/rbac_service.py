# Epic Title: Role-Based Access Control

from functools import wraps
from flask import request, redirect, url_for, flash
from flask_login import current_user
from backend.authorization.models.user_role_model import UserRole

class RBACService:
    @staticmethod
    def role_required(role: str):
        # Epic Title: Role-Based Access Control
        def decorator(func):
            @wraps(func)
            def decorated_view(*args, **kwargs):
                if not current_user.is_authenticated or not RBACService.user_has_role(current_user.id, role):
                    flash('You do not have the required role to access this resource')
                    return redirect(url_for('login'))
                return func(*args, **kwargs)
            return decorated_view
        return decorator
    
    @staticmethod
    def user_has_role(user_id: int, role: str) -> bool:
        # Epic Title: Role-Based Access Control
        user_role = UserRole.query.filter_by(user_id=user_id, role=role).first()
        return user_role is not None
    
    @staticmethod
    def assign_role_to_user(user_id: int, role_id: int) -> None:
        # Epic Title: Role-Based Access Control
        user_role = UserRole(user_id=user_id, role_id=role_id)
        user_role.save()