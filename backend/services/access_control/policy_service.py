# Epic Title: Role-based Access Control

from backend.models.access_control.policy_model import Policy
from backend.repositories.access_control.policy_repository import PolicyRepository

class PolicyService:
    @staticmethod
    def create_policy(name: str, role_id: int, action: str) -> Policy:
        policy = Policy(name=name, role_id=role_id, action=action)
        PolicyRepository.save(policy)
        return policy

    @staticmethod
    def get_policies_by_role(role_id: int) -> list[Policy]:
        return PolicyRepository.find_by_role_id(role_id)

# File 4: Policy Controller in controllers/access_control/policy_controller.py