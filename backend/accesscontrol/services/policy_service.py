# Epic Title: Access Policies for Different Roles

from backend.accesscontrol.repositories.policy_repository import PolicyRepository
from backend.accesscontrol.models.policy_model import Policy

class PolicyService:
    @staticmethod
    def create_policy(role_id: int, resource: str, can_view: bool, can_edit: bool, can_delete: bool) -> Policy:
        policy = Policy(role_id, resource, can_view, can_edit, can_delete)
        PolicyRepository.save(policy)
        return policy

    @staticmethod
    def get_policies_for_role(role_id: int) -> list[Policy]:
        return PolicyRepository.get_by_role_id(role_id)

    @staticmethod
    def check_access(role_id: int, resource: str, action: str) -> bool:
        policy = PolicyRepository.get_policy(role_id, resource)
        if policy:
            if action == 'view' and policy.can_view:
                return True
            if action == 'edit' and policy.can_edit:
                return True
            if action == 'delete' and policy.can_delete:
                return True
        return False


# File 4: Policy Controller for Handling Requests in accesscontrol/controllers/policy_controller.py