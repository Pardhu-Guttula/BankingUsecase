# Epic Title: Role-based Access Control

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.access_control.services.policy_service import PolicyService

policy_controller = Blueprint('policy_controller', __name__)

@policy_controller.route('/policies', methods=['POST'])
@login_required
def create_policy():
    data = request.get_json()
    policy_name = data.get('name')
    description = data.get('description', "")

    if not policy_name:
        return jsonify({"message": "Policy name is required"}), 400

    if PolicyService.create_policy(policy_name, description):
        return jsonify({"message": "Policy created successfully"}), 201
    return jsonify({"message": "Policy already exists"}), 409

@policy_controller.route('/policies', methods=['GET'])
@login_required
def get_policies():
    policies = PolicyService.get_all_policies()
    return jsonify([{"id": policy.id, "name": policy.name, "description": policy.description} for policy in policies]), 200

@policy_controller.route('/policies/assign', methods=['POST'])
@login_required
def assign_policy():
    data = request.get_json()
    role_id = data.get('role_id')
    policy_id = data.get('policy_id')

    if not role_id or not policy_id:
        return jsonify({"message": "Role ID and Policy ID are required"}), 400

    PolicyService.assign_policy(role_id, policy_id)
    return jsonify({"message": "Policy assigned successfully"}), 200

@policy_controller.route('/policies/remove', methods=['POST'])
@login_required
def remove_policy():
    data = request.get_json()
    role_id = data.get('role_id')
    policy_id = data.get('policy_id')

    if not role_id or not policy_id:
        return jsonify({"message": "Role ID and Policy ID are required"}), 400

    PolicyService.remove_policy(role_id, policy_id)
    return jsonify({"message": "Policy removed successfully"}), 200


# File 7: Middleware for Policy Enforcement in middleware/policy_enforcer.py