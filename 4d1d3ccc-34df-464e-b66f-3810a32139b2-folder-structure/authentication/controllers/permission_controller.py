# Epic Title: Role-based Access Control

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from authentication.services.permission_service import PermissionService
from authentication.decorators.access_policy_decorator import requires_permission

permission_controller = Blueprint('permission_controller', __name__)

@permission_controller.route('/permissions', methods=['POST'])
@login_required
@requires_permission('manage_permissions')
def define_permission():
    if not current_user.is_admin:
        return jsonify({"error": "Access denied"}), 403

    data = request.json
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({"error": "Permission name is required"}), 400

    permission = PermissionService.define_permission(name, description)
    return jsonify({"id": permission.id, "name": permission.name, "description": permission.description}), 201

@permission_controller.route('/permissions', methods=['GET'])
@login_required
@requires_permission('view_permissions')
def get_all_permissions():
    permissions = PermissionService.get_all_permissions()
    return jsonify([{"id": permission.id, "name": permission.name, "description": permission.description} for permission in permissions]), 200


# File 5: App Update to Register Permission Controller in app.py