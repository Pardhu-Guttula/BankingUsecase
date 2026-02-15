# Epic Title: Account Opening and Service Modifications

from backend.models.approval_workflow.approval_model import ApprovalWorkflow
from backend.repositories.approval_workflow.approval_workflow_repository import ApprovalWorkflowRepository

class ApprovalWorkflowService:
    @staticmethod
    def submit_for_approval(request_id: int, request_type: str) -> ApprovalWorkflow:
        approval_workflow = ApprovalWorkflow(request_id=request_id, request_type=request_type)
        ApprovalWorkflowRepository.save(approval_workflow)
        return approval_workflow

    @staticmethod
    def get_approval_status(request_id: int, request_type: str) -> ApprovalWorkflow:
        return ApprovalWorkflowRepository.get_approval_by_request_id(request_id, request_type)

    @staticmethod
    def update_approval_status(request_id: int, request_type: str, status: str) -> None:
        approval_workflow = ApprovalWorkflowRepository.get_approval_by_request_id(request_id, request_type)
        if approval_workflow:
            approval_workflow.status = status
            ApprovalWorkflowRepository.update(approval_workflow)

# File 4: Approval Workflow Controller to Handle Approvals in approval_workflow/controllers/approval_controller.py