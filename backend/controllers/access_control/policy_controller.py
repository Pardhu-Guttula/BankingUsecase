# Epic Title: Role-based Access Control

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.access_control.policy_service import PolicyService

policy_controller = Blueprint('policy_controller', __name__)

@policy_controller.route('/policies', methods=['POST'])
@login_required
def create_policy():
    if not current_user.is_admin:
        return jsonify({'message': 'Permission denied'}), 403

    data = request.get_json()
    name = data.get('name')
    role_id = data.get('role_id')
    action = data.get('action')

    if not name or not role_id or not action:
        return jsonify({'message': 'Name, role ID, and action are required'}), 400

    policy = PolicyService.create_policy(name, role_id, action)
    return jsonify({
        'id': policy.id,
        'name': policy.name,
        'role_id': policy.role_id,
        'action': policy.action
    }), 201

@policy_controller.route('/policies/<int:role_id>', methods=['GET'])
@login_required
def get_policies_by_role(role_id: int):
    policies = PolicyService.get_policies_by_role(role_id)
    return jsonify([{
        'id': policy.id,
        'name': policy.name,
        'role_id': policy.role_id,
        'action': policy.action
    } for policy in policies])

# File 5: User Model Updated for Policy Check in models/access_control/user_model.py (Modified)