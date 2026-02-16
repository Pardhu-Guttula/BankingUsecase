# Epic Title: Role-based Access Control

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.rbac.services import RoleService

rbac_blueprint = Blueprint('rbac', __name__)
# Initialize RoleService later in app.py to inject dependencies
role_service = None  # Placeholder for real instance

@rbac_blueprint.route('/roles', methods=['POST'])
@jwt_required()
def create_role():
    current_user_id = get_jwt_identity()
    if not is_admin(current_user_id):
        return jsonify({"error": "Unauthorized"}), 403

    name = request.json.get('name')
    description = request.json.get('description', "")
    if not name:
        return jsonify({"error": "Role name is required"}), 400

    try:
        role = role_service.create_role(name, description)
        return jsonify({"message": "Role created successfully", "role": {"id": role.id, "name": role.name, "description": role.description}}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@rbac_blueprint.route('/roles/assign', methods=['POST'])
@jwt_required()
def assign_role():
    current_user_id = get_jwt_identity()
    if not is_admin(current_user_id):
        return jsonify({"error": "Unauthorized"}), 403

    user_id = request.json.get('user_id')
    role_id = request.json.get('role_id')
    if not user_id or not role_id:
        return jsonify({"error": "User ID and Role ID are required"}), 400

    try:
        user_role = role_service.assign_role_to_user(user_id, role_id)
        return jsonify({"message": "Role assigned successfully", "user_role": {"id": user_role.id, "user_id": user_role.user_id, "role_id": user_role.role_id}}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@rbac_blueprint.route('/roles', methods=['GET'])
@jwt_required()
def get_roles():
    roles = role_service.get_roles()
    return jsonify([{"id": role.id, "name": role.name, "description": role.description} for role in roles]), 200

@rbac_blueprint.route('/permissions', methods=['POST'])
@jwt_required()
def create_permission():
    current_user_id = get_jwt_identity()
    if not is_admin(current_user_id):
        return jsonify({"error": "Unauthorized"}), 403

    name = request.json.get('name')
    description = request.json.get('description', "")
    if not name:
        return jsonify({"error": "Permission name is required"}), 400

    try:
        permission = role_service.create_permission(name, description)
        return jsonify({"message": "Permission created successfully", "permission": {"id": permission.id, "name": permission.name, "description": permission.description}}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@rbac_blueprint.route('/permissions/assign', methods=['POST'])
@jwt_required()
def assign_permission():
    current_user_id = get_jwt_identity()
    if not is_admin(current_user_id):
        return jsonify({"error": "Unauthorized"}), 403

    role_id = request.json.get('role_id')
    permission_id = request.json.get('permission_id')
    if not role_id or not permission_id:
        return jsonify({"error": "Role ID and Permission ID are required"}), 400

    try:
        role_permission = role_service.assign_permission_to_role(role_id, permission_id)
        return jsonify({"message": "Permission assigned successfully", "role_permission": {"id": role_permission.id, "role_id": role_permission.role_id, "permission_id": role_permission.permission_id}}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@rbac_blueprint.route('/permissions', methods=['GET'])
@jwt_required()
def get_permissions():
    permissions = role_service.get_permissions()
    return jsonify([{"id": permission.id, "name": permission.name, "description": permission.description} for permission in permissions]), 200

@rbac_blueprint.route('/access', methods=['GET'])
@jwt_required()
def check_access():
    current_user_id = get_jwt_identity()
    endpoint = request.args.get('endpoint')
    
    if not endpoint:
        return jsonify({"error": "Endpoint is required"}), 400

    permissions = role_service.get_user_permissions(current_user_id)
    permission_names = [permission.name for permission in permissions]

    if endpoint in permission_names:
        return jsonify({"access": "granted"}), 200
    else:
        return jsonify({"access": "denied"}), 403