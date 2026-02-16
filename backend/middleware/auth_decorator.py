# Epic Title: Role-based Access Control

from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from backend.access_control.models.role import UserRole
from backend.access_control.models.permission import RolePermission

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        user_id = get_jwt_identity()

        user_roles = UserRole.query.filter_by(user_id=user_id).all()
        roles = [user_role.role.name for user_role in user_roles]

        if 'admin' not in roles:
            return jsonify(msg="Admins only!"), 403

        return fn(*args, **kwargs)
    
    return wrapper

def permission_required(permission_name):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            user_id = get_jwt_identity()

            user_roles = UserRole.query.filter_by(user_id=user_id).all()
            role_ids = [user_role.role_id for user_role in user_roles]
            permissions = RolePermission.query.filter(RolePermission.role_id.in_(role_ids)).all()

            permission_names = [p.permission.name for p in permissions]

            if permission_name not in permission_names:
                return jsonify(msg=f"Permission '{permission_name}' required!"), 403

            return fn(*args, **kwargs)
        
        return wrapper
    
    return decorator