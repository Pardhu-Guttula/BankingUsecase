# Epic Title: Role-based Access Control

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from authentication.services.role_service import RoleService

role_controller = Blueprint('role_controller', __name__)

@role_controller.route('/roles', methods=['POST'])
@login_required
def define_role():
    if not current_user.is_admin:
        return jsonify({"error": "Access denied"}), 403

    data = request.json
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({"error": "Role name is required"}), 400

    role = RoleService.define_role(name, description)
    return jsonify({"id": role.id, "name": role.name, "description": role.description}), 201

@role_controller.route('/roles', methods=['GET'])
@login_required
def get_all_roles():
    roles = RoleService.get_all_roles()
    return jsonify([{"id": role.id, "name": role.name, "description": role.description} for role in roles]), 200


# File 6: App Update to Register Role Controller in app.py