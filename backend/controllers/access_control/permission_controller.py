# Epic Title: Assign Permissions to Roles

from flask import Blueprint, request, jsonify
from flask_login import login_required
from backend.services.access_control.role_permission_service import RolePermissionService
from backend.models.access_control.permission_model import Permission
from backend.repositories.access_control.permission_repository import PermissionRepository

permission_controller = Blueprint('permission_controller', __name__)

@permission_controller.route('/permissions', methods=['POST'])
@login_required
def create_permission():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'message': 'Permission name is required'}), 400

    try:
        permission = Permission(name=name, description=description)
        PermissionRepository.save(permission)
        return jsonify({'message': 'Permission created successfully', 'permission': permission.id}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@permission_controller.route('/permissions/<int:permission_id>', methods=['GET'])
@login_required
def get_permission(permission_id: int):
    try:
        permission = PermissionRepository.find_by_id(permission_id)
        if permission:
            return jsonify({'id': permission.id, 'name': permission.name, 'description': permission.description}), 200
        else:
            return jsonify({'message': 'Permission not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@permission_controller.route('/permissions', methods=['GET'])
@login_required
def get_all_permissions():
    try:
        permissions = PermissionRepository.find_all()
        return jsonify([{'id': permission.id, 'name': permission.name, 'description': permission.description} for permission in permissions]), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@permission_controller.route('/roles/<int:role_id>/permissions', methods=['POST'])
@login_required
def assign_permission_to_role(role_id: int):
    data = request.get_json()
    permission_id = data.get('permission_id')

    if not permission_id:
        return jsonify({'message': 'Permission ID is required'}), 400

    try:
        RolePermissionService.assign_permission_to_role(role_id, permission_id)
        return jsonify({'message': 'Permission assigned to role successfully'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@permission_controller.route('/roles/<int:role_id>/permissions/<int:permission_id>', methods=['DELETE'])
@login_required
def remove_permission_from_role(role_id: int, permission_id: int):
    try:
        RolePermissionService.remove_permission_from_role(role_id, permission_id)
        return jsonify({'message': 'Permission removed from role successfully'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@permission_controller.route('/roles/<int:role_id>/permissions', methods=['GET'])
@login_required
def get_permissions_by_role(role_id: int):
    try:
        role_permissions = RolePermissionService.get_permissions_by_role(role_id)
        return jsonify([{'role_id': role_permission.role_id, 'permission_id': role_permission.permission_id} for role_permission in role_permissions]), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500


# File 7: Schema for Role-Permission and Permissions Tables in `database/create_role_permission_tables.sql`