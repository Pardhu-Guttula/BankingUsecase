# Epic Title: Role-based Access Control

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from backend.services.access_control.policy_service import PolicyService

policy_controller = Blueprint('policy_controller', __name__)

@policy_controller.route('/policies', methods=['POST'])
@login_required
def create_policy():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'message': 'Policy name is required'}), 400

    policy = PolicyService.create_policy(name, description)
    return jsonify({
        'id': policy.id,
        'name': policy.name,
        'description': policy.description
    }), 201

@policy_controller.route('/policies', methods=['GET'])
@login_required
def get_policies():
    policies = PolicyService.get_policies()
    policies_list = [{'id': policy.id, 'name': policy.name, 'description': policy.description} for policy in policies]
    return jsonify(policies_list)

@policy_controller.route('/policies/assign', methods=['POST'])
@login_required
def assign_policy():
    data = request.get_json()
    role_id = data.get('role_id')
    policy_id = data.get('policy_id')

    if not role_id or not policy_id:
        return jsonify({'message': 'Role ID and Policy ID are required'}), 400

    role_policy = PolicyService.assign_policy_to_role(role_id, policy_id)
    return jsonify({
        'id': role_policy.id,
        'role_id': role_policy.role_id,
        'policy_id': role_policy.policy_id
    }), 201

@policy_controller.route('/roles/<int:role_id>/policies', methods=['GET'])
@login_required
def get_role_policies(role_id: int):
    role_policies = PolicyService.get_role_policies(role_id)
    role_policies_list = [{'id': role_policy.id, 'role_id': role_policy.role_id, 'policy_id': role_policy.policy_id} for role_policy in role_policies]
    return jsonify(role_policies_list)

# File 7: Register Policy Controller Blueprint in app.py (Already Exists, Modified)