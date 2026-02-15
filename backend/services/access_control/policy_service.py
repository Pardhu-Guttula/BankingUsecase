# Epic Title: Access Policies for Different Roles

from backend.repositories.access_control.policy_repository import PolicyRepository
from backend.models.access_control.policy_model import Policy

class PolicyService:
    @staticmethod
    def create_policy(role_id: int, service_name: str, action: str) -> Policy:
        policy = Policy(role_id=role_id, service_name=service_name, action=action)
        PolicyRepository.save(policy)
        return policy

    @staticmethod
    def get_policy_by_id(policy_id: int) -> Policy:
        return PolicyRepository.find_by_id(policy_id)

    @staticmethod
    def get_policies_by_role(role_id: int) -> list[Policy]:
        return PolicyRepository.find_by_role_id(role_id)

    @staticmethod
    def get_all_policies() -> list[Policy]:
        return PolicyRepository.find_all()


# File 4: Policy Controller in `controllers/access_control/policy_controller.py`