# Epic Title: Role-based Access Control

from backend.access_control.roles.policy_repository import PolicyRepository
from backend.access_control.roles.role_policy_repository import RolePolicyRepository
from backend.models.access_control.policy_model import Policy
from flask import current_app

class PolicyService:
    @staticmethod
    def create_policy(name: str, description: str = None) -> bool:
        if PolicyRepository.get_policy_by_name(name):
            return False
        new_policy = Policy(name=name, description=description)
        PolicyRepository.save(new_policy)
        return True

    @staticmethod
    def get_all_policies() -> list[Policy]:
        return PolicyRepository.get_all_policies()

    @staticmethod
    def assign_policy(role_id: int, policy_id: int) -> None:
        RolePolicyRepository.assign_policy_to_role(role_id, policy_id)

    @staticmethod
    def remove_policy(role_id: int, policy_id: int) -> None:
        RolePolicyRepository.remove_policy_from_role(role_id, policy_id)


# File 6: Policy Controller to Expose Endpoints for Policy Management in access_control/controllers/policy_controller.py