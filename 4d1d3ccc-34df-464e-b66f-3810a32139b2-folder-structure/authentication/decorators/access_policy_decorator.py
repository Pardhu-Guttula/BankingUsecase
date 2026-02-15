# Epic Title: Role-based Access Control

from functools import wraps
from flask import request, jsonify
from authentication.services.access_policy_service import AccessPolicyService

def requires_permission(permission_name):
    def decorator(func):
        @wraps(func)
        def wrapped_view(*args, **kwargs):
            if not AccessPolicyService.has_permission(permission_name):
                return jsonify({"error": "Access denied"}), 403
            return func(*args, **kwargs)
        return wrapped_view
    return decorator


# File 3: Role Controller Update to Include Access Policy in authentication/controllers/role_controller.py