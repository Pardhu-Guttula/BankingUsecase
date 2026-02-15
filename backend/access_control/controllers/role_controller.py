# Epic Title: Role-based Access Control

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.access_control.role_service import RoleService
from backend.models.authentication.user_model import User

role_controller = Blueprint('role_controller', __name__)

@role_controller.route('/roles', methods=['POST'])
@login_required
def create_role():
    data = request.get_json()
    role = RoleService.create_role(data['name'], data.get('description', ''))
    return jsonify({"message": "Role created successfully", "role": role.name}), 201

@role_controller.route('/roles/<int:role_id>', methods=['PUT'])
@login_required
def update_role(role_id):
    data = request.get_json()
    role = RoleService.update_role(role_id, data.get('name'), data.get('description'))
    return jsonify({"message": "Role updated successfully", "role": role.name}), 200

@role_controller.route('/roles/<int:role_id>', methods=['DELETE'])
@login_required
def delete_role(role_id):
    RoleService.delete_role(role_id)
    return jsonify({"message": "Role deleted successfully"}), 200

@role_controller.route('/assign_role/<int:user_id>/<int:role_id>', methods=['POST'])
@login_required
def assign_role(user_id, role_id):
    user = User.query.get(user_id)
    RoleService.assign_role_to_user(user, role_id)
    return jsonify({"message": "Role assigned successfully"}), 200

@role_controller.route('/remove_role/<int:user_id>', methods=['POST'])
@login_required
def remove_role(user_id):
    user = User.query.get(user_id)
    RoleService.remove_role_from_user(user)
    return jsonify({"message": "Role removed successfully"}), 200


# File 6: Update Main App to Register Role Controller in app.py