# Epic Title: Role-based Access Control

from backend.models.access_control.policy_model import Policy
from backend.app import db

class PolicyRepository:
    @staticmethod
    def save(policy: Policy) -> None:
        db.session.add(policy)
        db.session.commit()

    @staticmethod
    def find_all() -> list[Policy]:
        return Policy.query.all()

    @staticmethod
    def find_by_role_id(role_id: int) -> list[Policy]:
        return Policy.query.filter_by(role_id=role_id).all()

# File 3: Policy Service in services/access_control/policy_service.py