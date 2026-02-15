# Epic Title: Access Policies for Different Roles

from backend.accesscontrol.models.policy_model import Policy
from backend.app import db

class PolicyRepository:
    @staticmethod
    def save(policy: Policy) -> None:
        db.session.add(policy)
        db.session.commit()

    @staticmethod
    def get_by_role_id(role_id: int) -> list[Policy]:
        return Policy.query.filter_by(role_id=role_id).all()

    @staticmethod
    def get_policy(role_id: int, resource: str) -> Policy:
        return Policy.query.filter_by(role_id=role_id, resource=resource).first()


# File 3: Policy Service for Business Logic in accesscontrol/services/policy_service.py