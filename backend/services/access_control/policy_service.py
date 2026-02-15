# Epic Title: Role-based Access Control

from backend.repositories.access_control.policy_repository import PolicyRepository
from backend.models.access_control.policy_model import Policy

class PolicyService:
    @staticmethod
    def create_policy(role_id: int, service_name: str, access_level: str) -> Policy:
        policy = Policy(role_id, service_name, access_level)
        PolicyRepository.save(policy)
        return policy

    @staticmethod
    def get_policies_by_role(role_id: int) -> list[Policy]:
        return PolicyRepository.find_by_role_id(role_id)

    @staticmethod
    def get_all_policies() -> list[Policy]:
        return PolicyRepository.find_all()


# File 5: Policy Form to Capture Policy Data in forms/policy_form.py