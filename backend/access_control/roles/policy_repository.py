# Epic Title: Role-based Access Control

from backend.models.access_control.policy_model import Policy
from backend.app import db

class PolicyRepository:
    @staticmethod
    def save(policy: Policy) -> None:
        db.session.add(policy)
        db.session.commit()

    @staticmethod
    def get_all_policies() -> list[Policy]:
        return Policy.query.all()

    @staticmethod
    def get_policy_by_name(policy_name: str) -> Policy:
        return Policy.query.filter_by(name=policy_name).first()

    @staticmethod
    def delete(policy: Policy) -> None:
        db.session.delete(policy)
        db.session.commit()


# File 4: RolePolicy Repository to Associate Roles and Policies in access_control/roles/role_policy_repository.py