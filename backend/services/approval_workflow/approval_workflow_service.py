# Epic Title: Approval and Processing Workflows

from backend.repositories.approval_workflow.approval_workflow_repository import ApprovalWorkflowRepository
from backend.models.approval_workflow.approval_workflow_model import ApprovalWorkflow

class ApprovalWorkflowService:
    @staticmethod
    def create_workflow(request_id: int, request_type: str, approver_id: int) -> None:
        workflow = ApprovalWorkflow(request_id=request_id, request_type=request_type, approver_id=approver_id)
        ApprovalWorkflowRepository.save(workflow)

    @staticmethod
    def approve_workflow(workflow_id: int, comments: str = None) -> None:
        workflow = ApprovalWorkflow.query.get(workflow_id)
        if workflow:
            workflow.status = 'Approved'
            workflow.approval_date = datetime.utcnow()
            workflow.comments = comments
            ApprovalWorkflowRepository.update(workflow)

    @staticmethod
    def reject_workflow(workflow_id: int, comments: str = None) -> None:
        workflow = ApprovalWorkflow.query.get(workflow_id)
        if workflow:
            workflow.status = 'Rejected'
            workflow.approval_date = datetime.utcnow()
            workflow.comments = comments
            ApprovalWorkflowRepository.update(workflow)

    @staticmethod
    def get_workflows_by_request(request_id: int, request_type: str) -> list:
        return ApprovalWorkflowRepository.find_by_request_id(request_id, request_type)


# File 4: Approval Workflow Controller in controllers/approval_workflow/approval_workflow_controller.py