# Epic Title: Role-based Access Control

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.access_control.services.permission_service import PermissionService

permission_controller = Blueprint('permission_controller', __name__)

@permission_controller.route('/permissions', methods=['POST'])
@login_required
def create_permission():
    data = request.get_json()
    permission_name = data.get('name')
    description = data.get('description', "")

    if not permission_name:
        return jsonify({"message": "Permission name is required"}), 400

    if PermissionService.create_permission(permission_name, description):
        return jsonify({"message": "Permission created successfully"}), 201
    return jsonify({"message": "Permission already exists"}), 409

@permission_controller.route('/permissions', methods=['GET'])
@login_required
def get_permissions():
    permissions = PermissionService.get_all_permissions()
    return jsonify([{"id": permission.id, "name": permission.name, "description": permission.description} for permission in permissions]), 200

@permission_controller.route('/permissions/assign', methods=['POST'])
@login_required
def assign_permission():
    data = request.get_json()
    role_id = data.get('role_id')
    permission_id = data.get('permission_id')

    if not role_id or not permission_id:
        return jsonify({"message": "Role ID and Permission ID are required"}), 400

    PermissionService.assign_permission(role_id, permission_id)
    return jsonify({"message": "Permission assigned successfully"}), 200

@permission_controller.route('/permissions/remove', methods=['POST'])
@login_required
def remove_permission():
    data = request.get_json()
    role_id = data.get('role_id')
    permission_id = data.get('permission_id')

    if not role_id or not permission_id:
        return jsonify({"message": "Role ID and Permission ID are required"}), 400

    PermissionService.remove_permission(role_id, permission_id)
    return jsonify({"message": "Permission removed successfully"}), 200


# File 7: Update Main App to Register Permission Controller in app.py