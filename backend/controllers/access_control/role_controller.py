# Epic Title: Role-based Access Control

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.access_control.role_service import RoleService

role_controller = Blueprint('role_controller', __name__)

@role_controller.route('/roles', methods=['POST'])
@login_required
def create_role():
    if not current_user.is_admin:
        return jsonify({'message': 'Permission denied'}), 403

    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'message': 'Role name is required'}), 400

    role = RoleService.create_role(name, description)
    return jsonify({
        'id': role.id,
        'name': role.name,
        'description': role.description
    }), 201

@role_controller.route('/roles', methods=['GET'])
@login_required
def get_all_roles():
    roles = RoleService.get_all_roles()
    return jsonify([{
        'id': role.id,
        'name': role.name,
        'description': role.description
    } for role in roles])

@role_controller.route('/roles/assign_permissions', methods=['POST'])
@login_required
def assign_permissions():
    if not current_user.is_admin:
        return jsonify({'message': 'Permission denied'}), 403

    data = request.get_json()
    role_name = data.get('role_name')
    permission_names = data.get('permission_names')

    if not role_name or not permission_names:
        return jsonify({'message': 'Role name and permissions are required'}), 400

    role = RoleService.assign_permissions(role_name, permission_names)
    if not role:
        return jsonify({'message': 'Role not found'}), 404

    return jsonify({
        'id': role.id,
        'name': role.name,
        'permissions': [perm.name for perm in role.permissions]
    }), 200

# File 6: User Model Updated for Permission Check in models/access_control/user_model.py (Modified)