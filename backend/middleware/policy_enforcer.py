# Epic Title: Role-based Access Control

from functools import wraps
from flask import request, jsonify
from flask_login import current_user
from backend.access_control.services.role_service import RoleService

def policy_required(policy_name: str):
    def decorator(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                return jsonify({"message": "Authentication required"}), 403
            if not RoleService.has_policy(current_user.id, policy_name):
                return jsonify({"message": "Access denied for missing required policy"}), 403
            return func(*args, **kwargs)
        return decorated_view
    return decorator


# File 8: Update Main App to Register Policy Controller and Middleware in app.py