# Epic Title: Approval and Processing Workflows

from dashboard.repositories.approval_workflow_repository import ApprovalWorkflowRepository
from dashboard.models.approval_workflow_model import ApprovalWorkflow

class ApprovalWorkflowService:
    @staticmethod
    def create_workflow(request_type: str, request_id: int, approver_id: int) -> ApprovalWorkflow:
        workflow = ApprovalWorkflow(request_type, request_id, approver_id)
        ApprovalWorkflowRepository.save(workflow)
        return workflow

    @staticmethod
    def process_workflow(request_type: str, request_id: int, approver_id: int, approved: bool) -> str:
        workflow = ApprovalWorkflowRepository.get_workflow_by_request(request_type, request_id)
        if not workflow or workflow.approver_id != approver_id:
            return "Invalid request or approver"
        
        status = "approved" if approved else "rejected"
        ApprovalWorkflowRepository.update_status(workflow, status)
        return status


# File 4: Approval Workflow Controller for Handling Requests in dashboard/controllers/approval_workflow_controller.py