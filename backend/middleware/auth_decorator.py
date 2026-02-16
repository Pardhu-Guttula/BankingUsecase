# Epic Title: Role-based Access Control

from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from backend.access_control.models.role import UserRole

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