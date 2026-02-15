# Epic Title: Role-based Access Control

from backend.models.access_control.role_policy_model import RolePolicy
from backend.app import db

class RolePolicyRepository:
    @staticmethod
    def assign_policy_to_role(role_id: int, policy_id: int) -> None:
        role_policy = RolePolicy(role_id=role_id, policy_id=policy_id)
        db.session.add(role_policy)
        db.session.commit()

    @staticmethod
    def remove_policy_from_role(role_id: int, policy_id: int) -> None:
        role_policy = RolePolicy.query.filter_by(role_id=role_id, policy_id=policy_id).first()
        if role_policy:
            db.session.delete(role_policy)
            db.session.commit()


# File 5: Policy Service for Business Logic in access_control/services/policy_service.py