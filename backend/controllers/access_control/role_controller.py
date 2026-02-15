# Epic Title: Define User Roles

from flask import Blueprint, request, jsonify
from flask_login import login_required
from backend.services.access_control.role_service import RoleService

role_controller = Blueprint('role_controller', __name__)

@role_controller.route('/roles', methods=['POST'])
@login_required
def create_role():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'message': 'Role name is required'}), 400

    try:
        role = RoleService.create_role(name, description)
        return jsonify({'message': 'Role created successfully', 'role': role.id}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@role_controller.route('/roles/<int:role_id>', methods=['PUT'])
@login_required
def update_role(role_id: int):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'message': 'Role name is required'}), 400

    try:
        role = RoleService.update_role(role_id, name, description)
        if role:
            return jsonify({'message': 'Role updated successfully'}), 200
        else:
            return jsonify({'message': 'Role not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@role_controller.route('/roles/<int:role_id>', methods=['DELETE'])
@login_required
def delete_role(role_id: int):
    try:
        RoleService.delete_role(role_id)
        return jsonify({'message': 'Role deleted successfully'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@role_controller.route('/roles/<int:role_id>', methods=['GET'])
@login_required
def get_role(role_id: int):
    try:
        role = RoleService.get_role(role_id)
        if role:
            return jsonify({'id': role.id, 'name': role.name, 'description': role.description}), 200
        else:
            return jsonify({'message': 'Role not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@role_controller.route('/roles', methods=['GET'])
@login_required
def get_all_roles():
    try:
        roles = RoleService.get_all_roles()
        return jsonify([{'id': role.id, 'name': role.name, 'description': role.description} for role in roles]), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500


# File 5: Schema for Roles Table in `database/create_roles_table.sql`