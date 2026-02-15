# Epic Title: Role-based Access Control

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from backend.services.access_control.permission_service import PermissionService

permission_controller = Blueprint('permission_controller', __name__)

@permission_controller.route('/permissions', methods=['POST'])
@login_required
def create_permission():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'message': 'Permission name is required'}), 400

    permission = PermissionService.create_permission(name, description)
    return jsonify({
        'id': permission.id,
        'name': permission.name,
        'description': permission.description
    }), 201

@permission_controller.route('/permissions', methods=['GET'])
@login_required
def get_permissions():
    permissions = PermissionService.get_permissions()
    permissions_list = [{'id': permission.id, 'name': permission.name, 'description': permission.description} for permission in permissions]
    return jsonify(permissions_list)

@permission_controller.route('/permissions/assign', methods=['POST'])
@login_required
def assign_permission():
    data = request.get_json()
    role_id = data.get('role_id')
    permission_id = data.get('permission_id')

    if not role_id or not permission_id:
        return jsonify({'message': 'Role ID and Permission ID are required'}), 400

    role_permission = PermissionService.assign_permission_to_role(role_id, permission_id)
    return jsonify({
        'id': role_permission.id,
        'role_id': role_permission.role_id,
        'permission_id': role_permission.permission_id
    }), 201

@permission_controller.route('/roles/<int:role_id>/permissions', methods=['GET'])
@login_required
def get_role_permissions(role_id: int):
    role_permissions = PermissionService.get_role_permissions(role_id)
    role_permissions_list = [{'id': role_permission.id, 'role_id': role_permission.role_id, 'permission_id': role_permission.permission_id} for role_permission in role_permissions]
    return jsonify(role_permissions_list)

# File 7: Register Permission Controller Blueprint in app.py (Already Exists, Modified)