# Epic Title: Access Policies for Different Roles

from flask import Blueprint, request, jsonify
from flask_login import login_required
from backend.services.access_control.policy_service import PolicyService

policy_controller = Blueprint('policy_controller', __name__)

@policy_controller.route('/policies', methods=['POST'])
@login_required
def create_policy():
    data = request.get_json()
    role_id = data.get('role_id')
    service_name = data.get('service_name')
    action = data.get('action')

    if not role_id or not service_name or not action:
        return jsonify({'message': 'Role ID, Service Name, and Action are required'}), 400

    try:
        policy = PolicyService.create_policy(role_id, service_name, action)
        return jsonify({'message': 'Policy created successfully', 'policy': policy.id}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@policy_controller.route('/policies/<int:policy_id>', methods=['GET'])
@login_required
def get_policy(policy_id: int):
    try:
        policy = PolicyService.get_policy_by_id(policy_id)
        if policy:
            return jsonify({'id': policy.id, 'role_id': policy.role_id, 'service_name': policy.service_name, 'action': policy.action}), 200
        else:
            return jsonify({'message': 'Policy not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@policy_controller.route('/policies/role/<int:role_id>', methods=['GET'])
@login_required
def get_policies_by_role(role_id: int):
    try:
        policies = PolicyService.get_policies_by_role(role_id)
        return jsonify([{'id': policy.id, 'role_id': policy.role_id, 'service_name': policy.service_name, 'action': policy.action} for policy in policies]), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@policy_controller.route('/policies', methods=['GET'])
@login_required
def get_all_policies():
    try:
        policies = PolicyService.get_all_policies()
        return jsonify([{'id': policy.id, 'role_id': policy.role_id, 'service_name': policy.service_name, 'action': policy.action} for policy in policies]), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500


# File 5: Schema for Policies Table in `database/create_policies_table.sql`