# Epic Title: Define User Roles

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from accesscontrol.services.role_service import RoleService

role_controller = Blueprint('role_controller', __name__)

@role_controller.route('/roles', methods=['POST'])
@login_required
def create_role():
    data = request.json
    name = data.get('name')

    if not name:
        return jsonify({"error": "Role name is required"}), 400

    role = RoleService.create_role(name)
    return jsonify({"id": role.id, "name": role.name}), 201

@role_controller.route('/roles/<int:user_id>/assign', methods=['POST'])
@login_required
def assign_role(user_id: int):
    data = request.json
    role_id = data.get('role_id')

    if not role_id:
        return jsonify({"error": "Role ID is required"}), 400

    RoleService.assign_role_to_user(user_id, role_id)
    return jsonify({"message": "Role assigned successfully"}), 200

@role_controller.route('/roles', methods=['GET'])
@login_required
def get_roles():
    roles = RoleService.get_all_roles()
    return jsonify([{"id": role.id, "name": role.name} for role in roles])


# File 7: App Update to Register Role Controller in app.py