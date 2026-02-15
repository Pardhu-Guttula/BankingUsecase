# Epic Title: Role-based Access Control

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.access_control.policy_service import PolicyService
from backend.repositories.access_control.policy_repository import PolicyRepository
from backend.models.access_control.policy_model import Policy

policy_controller = Blueprint('policy_controller', __name__)

@policy_controller.route('/policies', methods=['POST'])
@login_required
def create_policy():
    data = request.get_json()
    policy = PolicyService.create_policy(data['name'], data['description'], data['role_id'])
    return jsonify({"message": "Policy created successfully", "policy": policy.name}), 201

@policy_controller.route('/policies/<int:policy_id>', methods=['PUT'])
@login_required
def update_policy(policy_id):
    data = request.get_json()
    policy = PolicyService.update_policy(policy_id, data.get('name'), data.get('description'), data.get('is_active'))
    return jsonify({"message": "Policy updated successfully", "policy": policy.name}), 200

@policy_controller.route('/policies/<int:policy_id>', methods=['DELETE'])
@login_required
def delete_policy(policy_id):
    PolicyService.delete_policy(policy_id)
    return jsonify({"message": "Policy deleted successfully"}), 200


# File 6: Middleware to Enforce Policy Restrictions based on Roles in middleware/policy_middleware.py