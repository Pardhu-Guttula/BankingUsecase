# Epic Title: Role-based Access Control

from backend.repositories.access_control.policy_repository import PolicyRepository
from backend.models.access_control.policy_model import Policy

class PolicyService:
    @staticmethod
    def create_policy(name: str, description: str, role_id: int) -> Policy:
        policy = Policy(name=name, description=description, role_id=role_id)
        PolicyRepository.save(policy)
        return policy

    @staticmethod
    def update_policy(policy_id: int, name: str = None, description: str = None, is_active: bool = None) -> Policy:
        policy = PolicyRepository.get_policy_by_id(policy_id)
        if name is not None:
            policy.name = name
        if description is not None:
            policy.description = description
        if is_active is not None:
            policy.is_active = is_active
        PolicyRepository.update(policy)
        return policy

    @staticmethod
    def delete_policy(policy_id: int) -> None:
        policy = PolicyRepository.get_policy_by_id(policy_id)
        PolicyRepository.delete(policy)


# File 5: Policy Controller to Handle API Endpoints in access_control/controllers/policy_controller.py