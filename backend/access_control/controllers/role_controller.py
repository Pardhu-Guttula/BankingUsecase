# Epic Title: Role-based Access Control

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.access_control.services.role_service import RoleService
from backend.access_control.models.role import db

role_blueprint = Blueprint('roles', __name__)
role_service = RoleService()

@role_blueprint.route('/roles', methods=['POST'])
@jwt_required()
def create_role():
    data = request.json
    name = data.get('name')
    description = data.get('description')
    
    if not name:
        return jsonify({"error": "Role name is required"}), 400

    role = role_service.create_role(name, description)
    return jsonify({"id": role.id, "name": role.name, "description": role.description}), 201

@role_blueprint.route('/roles/assign', methods=['POST'])
@jwt_required()
def assign_role_to_user():
    data = request.json
    user_id = data.get('user_id')
    role_id = data.get('role_id')

    if not user_id or not role_id:
        return jsonify({"error": "User ID and Role ID are required"}), 400

    user_role = role_service.assign_role_to_user(user_id, role_id)
    return jsonify({"id": user_role.id, "user_id": user_role.user_id, "role_id": user_role.role_id}), 201

@role_blueprint.route('/roles', methods=['GET'])
@jwt_required()
def get_roles():
    roles = role_service.get_roles()
    return jsonify([{"id": role.id, "name": role.name, "description": role.description} for role in roles]), 200