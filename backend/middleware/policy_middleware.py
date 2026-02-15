# Epic Title: Role-based Access Control

from flask import g, request, jsonify
from flask_login import current_user
from backend.models.access_control.policy_model import Policy

class PolicyMiddleware:
    @staticmethod
    def enforce_policy():
        user_role_id = current_user.role_id
        policies = Policy.query.filter_by(role_id=user_role_id, is_active=True).all()

        for policy in policies:
            if not PolicyMiddleware.is_request_allowed(policy):
                return jsonify({"message": "Access restricted by policy"}), 403

    @staticmethod
    def is_request_allowed(policy: Policy) -> bool:
        # Define logic to determine if current request is allowed based on policy
        # For example, check if policy restricts access to certain endpoints or actions
        if policy.name == "restrict_access":
            if request.endpoint in policy.description.split(","):
                return False
        return True


# File 7: Update Main App to Register Policy Controller and Middleware in app.py