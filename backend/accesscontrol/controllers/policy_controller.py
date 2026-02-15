# Epic Title: Access Policies for Different Roles

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from accesscontrol.services.policy_service import PolicyService

policy_controller = Blueprint('policy_controller', __name__)

@policy_controller.route('/policies', methods=['POST'])
@login_required
def create_policy():
    data = request.json
    role_id = data.get('role_id')
    resource = data.get('resource')
    can_view = data.get('can_view', False)
    can_edit = data.get('can_edit', False)
    can_delete = data.get('can_delete', False)

    if not role_id or not resource:
        return jsonify({"error": "Role ID and resource are required"}), 400

    policy = PolicyService.create_policy(role_id, resource, can_view, can_edit, can_delete)
    return jsonify({
        "id": policy.id, 
        "role_id": policy.role_id,
        "resource": policy.resource,
        "can_view": policy.can_view,
        "can_edit": policy.can_edit,
        "can_delete": policy.can_delete
    }), 201

@policy_controller.route('/policies/<int:role_id>', methods=['GET'])
@login_required
def get_policies(role_id: int):
    policies = PolicyService.get_policies_for_role(role_id)
    return jsonify([{
        "id": policy.id,
        "resource": policy.resource,
        "can_view": policy.can_view,
        "can_edit": policy.can_edit,
        "can_delete": policy.can_delete
    } for policy in policies])


# File 5: Decorator for Enforcing Access Policies in accesscontrol/decorators/enforce_policy.py