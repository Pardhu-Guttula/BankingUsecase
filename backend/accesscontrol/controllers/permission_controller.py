# Epic Title: Assign Permissions to Roles

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from accesscontrol.services.permission_service import PermissionService

permission_controller = Blueprint('permission_controller', __name__)

@permission_controller.route('/permissions', methods=['POST'])
@login_required
def create_permission():
    data = request.json
    name = data.get('name')

    if not name:
        return jsonify({"error": "Permission name is required"}), 400

    permission = PermissionService.create_permission(name)
    return jsonify({"id": permission.id, "name": permission.name}), 201

@permission_controller.route('/permissions/<int:role_id>/assign', methods=['POST'])
@login_required
def assign_permission(role_id: int):
    data = request.json
    permission_id = data.get('permission_id')

    if not permission_id:
        return jsonify({"error": "Permission ID is required"}), 400

    PermissionService.assign_permission_to_role(role_id, permission_id)
    return jsonify({"message": "Permission assigned successfully"}), 200

@permission_controller.route('/permissions', methods=['GET'])
@login_required
def get_permissions():
    permissions = PermissionService.get_all_permissions()
    return jsonify([{"id": permission.id, "name": permission.name} for permission in permissions])


# File 7: App Update to Register Permission Controller in app.py