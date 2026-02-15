# Epic Title: Role-based Access Control

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.access_control.role_service import RoleService

role_controller = Blueprint('role_controller', __name__)

@role_controller.route('/roles', methods=['POST'])
@login_required
def create_role():
    if not current_user.is_admin:
        return jsonify({'message': 'Permission denied'}), 403

    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'message': 'Role name is required'}), 400

    role = RoleService.create_role(name, description)
    return jsonify({
        'id': role.id,
        'name': role.name,
        'description': role.description
    }), 201

@role_controller.route('/roles', methods=['GET'])
@login_required
def get_all_roles():
    roles = RoleService.get_all_roles()
    return jsonify([{
        'id': role.id,
        'name': role.name,
        'description': role.description
    } for role in roles])

# File 5: User Model in models/access_control/user_model.py (Modified)