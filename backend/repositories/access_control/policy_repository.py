# Epic Title: Role-based Access Control

from backend.models.access_control.policy_model import Policy
from backend.app import db

class PolicyRepository:
    @staticmethod
    def get_all_policies() -> list[Policy]:
        return Policy.query.all()

    @staticmethod
    def get_policy_by_id(policy_id: int) -> Policy:
        return Policy.query.get(policy_id)

    @staticmethod
    def save(policy: Policy) -> None:
        db.session.add(policy)
        db.session.commit()

    @staticmethod
    def update(policy: Policy) -> None:
        db.session.commit()

    @staticmethod
    def delete(policy: Policy) -> None:
        db.session.delete(policy)
        db.session.commit()


# File 4: Policy Service Layer to Handle Business Logic in services/access_control/policy_service.py