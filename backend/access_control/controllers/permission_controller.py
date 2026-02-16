# Epic Title: Role-based Access Control

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.access_control.services.permission_service import PermissionService
from backend.middleware.auth_decorator import admin_required

permission_blueprint = Blueprint('permissions', __name__)
permission_service = PermissionService()

@permission_blueprint.route('/permissions', methods=['POST'])
@jwt_required()
@admin_required
def create_permission():
    data = request.json
    name = data.get('name')
    description = data.get('description')
    
    if not name:
        return jsonify({"error": "Permission name is required"}), 400

    permission = permission_service.create_permission(name, description)
    return jsonify({"id": permission.id, "name": permission.name, "description": permission.description}), 201

@permission_blueprint.route('/permissions/assign', methods=['POST'])
@jwt_required()
@admin_required
def assign_permission_to_role():
    data = request.json
    role_id = data.get('role_id')
    permission_id = data.get('permission_id')

    if not role_id or not permission_id:
        return jsonify({"error": "Role ID and Permission ID are required"}), 400

    role_permission = permission_service.assign_permission_to_role(role_id, permission_id)
    return jsonify({"role_id": role_permission.role_id, "permission_id": role_permission.permission_id}), 201

@permission_blueprint.route('/permissions', methods=['GET'])
@jwt_required()
@admin_required
def get_permissions():
    permissions = permission_service.get_permissions()
    return jsonify([{"id": permission.id, "name": permission.name, "description": permission.description} for permission in permissions]), 200