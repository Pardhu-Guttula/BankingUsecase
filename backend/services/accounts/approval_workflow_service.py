# Epic Title: Account Opening and Service Modifications

from backend.repositories.accounts.approval_workflow_repository import ApprovalWorkflowRepository
from backend.models.accounts.approval_workflow_model import ApprovalWorkflow
from backend.models.accounts.account_opening_request_model import AccountOpeningRequest
from backend.models.accounts.service_modification_request_model import ServiceModificationRequest

class ApprovalWorkflowService:
    @staticmethod
    def initiate_workflow(request_id: int, request_type: str) -> ApprovalWorkflow:
        workflow = ApprovalWorkflow(request_id, request_type)
        ApprovalWorkflowRepository.save(workflow)
        return workflow

    @staticmethod
    def process_workflow(workflow: ApprovalWorkflow, status: str) -> None:
        workflow.status = status
        ApprovalWorkflowRepository.update(workflow)

    @staticmethod
    def get_workflow_by_request_id(request_id: int) -> ApprovalWorkflow:
        return ApprovalWorkflowRepository.find_by_request_id(request_id)


# File 4: Account Service Update to Integrate Approval Workflow in services/accounts/account_service.py