# Epic Title: Role-based Access Control

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from backend.services.access_control.role_service import RoleService

role_controller = Blueprint('role_controller', __name__)

@role_controller.route('/roles', methods=['POST'])
@login_required
def create_role():
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
def get_roles():
    roles = RoleService.get_roles()
    roles_list = [{'id': role.id, 'name': role.name, 'description': role.description} for role in roles]
    return jsonify(roles_list)

@role_controller.route('/roles/assign', methods=['POST'])
@login_required
def assign_role():
    data = request.get_json()
    user_id = data.get('user_id')
    role_id = data.get('role_id')

    if not user_id or not role_id:
        return jsonify({'message': 'User ID and Role ID are required'}), 400

    user_role = RoleService.assign_role_to_user(user_id, role_id)
    return jsonify({
        'id': user_role.id,
        'user_id': user_role.user_id,
        'role_id': user_role.role_id
    }), 201

@role_controller.route('/users/<int:user_id>/roles', methods=['GET'])
@login_required
def get_user_roles(user_id: int):
    user_roles = RoleService.get_user_roles(user_id)
    user_roles_list = [{'id': user_role.id, 'user_id': user_role.user_id, 'role_id': user_role.role_id} for user_role in user_roles]
    return jsonify(user_roles_list)

# File 7: Register Role Controller Blueprint in app.py (Already Exists, Modified)