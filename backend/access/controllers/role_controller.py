# Epic Title: Role-based Access Control

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.access_control.services.role_service import RoleService

role_controller = Blueprint('role_controller', __name__)

@role_controller.route('/roles', methods=['POST'])
@login_required
def create_role():
    data = request.get_json()
    role_name = data.get('name')
    description = data.get('description', "")

    if not role_name:
        return jsonify({"message": "Role name is required"}), 400

    if RoleService.create_role(role_name, description):
        return jsonify({"message": "Role created successfully"}), 201
    return jsonify({"message": "Role already exists"}), 409

@role_controller.route('/roles', methods=['GET'])
@login_required
def get_roles():
    roles = RoleService.get_all_roles()
    return jsonify([{"id": role.id, "name": role.name, "description": role.description} for role in roles]), 200

@role_controller.route('/roles/assign', methods=['POST'])
@login_required
def assign_role():
    data = request.get_json()
    user_id = data.get('user_id')
    role_id = data.get('role_id')

    if not user_id or not role_id:
        return jsonify({"message": "User ID and Role ID are required"}), 400

    RoleService.assign_role(user_id, role_id)
    return jsonify({"message": "Role assigned successfully"}), 200

@role_controller.route('/roles/remove', methods=['POST'])
@login_required
def remove_role():
    data = request.get_json()
    user_id = data.get('user_id')
    role_id = data.get('role_id')

    if not user_id or not role_id:
        return jsonify({"message": "User ID and Role ID are required"}), 400

    RoleService.remove_role(user_id, role_id)
    return jsonify({"message": "Role removed successfully"}), 200


# File 7: Update Main App to Register Role Controller in app.py