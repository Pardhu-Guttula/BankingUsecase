# Epic Title: Role-based Access Control

from backend.models.access_control.role_policy_model import RolePolicy
from backend.app import db

class RolePolicyRepository:
    @staticmethod
    def save(role_policy: RolePolicy) -> None:
        db.session.add(role_policy)
        db.session.commit()

    @staticmethod
    def get_policies_by_role(role_id: int) -> list[RolePolicy]:
        return RolePolicy.query.filter_by(role_id=role_id).all()

# File 5: Policy Management Service in services/access_control/policy_service.py