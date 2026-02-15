# Epic Title: Role-based Access Control

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.access_control.role_permission_service import RolePermissionService
from backend.repositories.access_control.permission_repository import PermissionRepository
from backend.models.access_control.permission_model import Permission

permission_controller = Blueprint('permission_controller', __name__)

@permission_controller.route('/permissions', methods=['POST'])
@login_required
def create_permission():
    data = request.get_json()
    permission = Permission(name=data['name'], description=data.get('description', ''))
    PermissionRepository.save(permission)
    return jsonify({"message": "Permission created successfully", "permission": permission.name}), 201

@permission_controller.route('/permissions/<int:permission_id>', methods=['PUT'])
@login_required
def update_permission(permission_id):
    data = request.get_json()
    permission = PermissionRepository.get_permission_by_id(permission_id)
    if not permission:
        return jsonify({"message": "Permission not found"}), 404
    if 'name' in data:
        permission.name = data['name']
    if 'description' in data:
        permission.description = data['description']
    PermissionRepository.update(permission)
    return jsonify({"message": "Permission updated successfully"}), 200

@permission_controller.route('/permissions/<int:permission_id>', methods=['DELETE'])
@login_required
def delete_permission(permission_id):
    permission = PermissionRepository.get_permission_by_id(permission_id)
    if not permission:
        return jsonify({"message": "Permission not found"}), 404
    PermissionRepository.delete(permission)
    return jsonify({"message": "Permission deleted successfully"}), 200

@permission_controller.route('/assign_permission/<int:role_id>/<int:permission_id>', methods=['POST'])
@login_required
def assign_permission(role_id, permission_id):
    RolePermissionService.assign_permission(role_id, permission_id)
    return jsonify({"message": "Permission assigned successfully"}), 200

@permission_controller.route('/remove_permission/<int:role_id>/<int:permission_id>', methods=['POST'])
@login_required
def remove_permission(role_id, permission_id):
    RolePermissionService.remove_permission(role_id, permission_id)
    return jsonify({"message": "Permission removed successfully"}), 200


# File 8: Update Main App to Register Permission Controller in app.py