# Epic Title: Access Policies for Different Roles

from functools import wraps
from flask import request, jsonify
from flask_login import current_user
from accesscontrol.services.policy_service import PolicyService
from accesscontrol.services.role_service import RoleService

def enforce_policy(resource: str, action: str):
    def decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            user_id = current_user.id
            roles = RoleService.get_roles_for_user(user_id)
            access_granted = any(PolicyService.check_access(role.role_id, resource, action) for role in roles)
            
            if not access_granted:
                return jsonify({"error": "Access denied"}), 403

            return func(*args, **kwargs)
        return wrapped_function
    return decorator


# File 6: App Update to Register Policy Controller in app.py