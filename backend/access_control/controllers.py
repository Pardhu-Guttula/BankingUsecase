# Epic Title: Role-based Access Control

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.access_control.services import RoleService

role_blueprint = Blueprint('roles', __name__)
# Initialize RoleService later in app.py to inject dependencies
role_service = None  # Placeholder for real instance

@role_blueprint.route('/roles', methods=['POST'])
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

@role_blueprint.route('/roles/assign', methods=['POST'])
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

@role_blueprint.route('/roles', methods=['GET'])
@jwt_required()
def get_roles():
    roles = role_service.get_roles()
    return jsonify([{"id": role.id, "name": role.name, "description": role.description} for role in roles]), 200