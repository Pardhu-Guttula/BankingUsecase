# Epic Title: Account Opening and Service Modifications

from backend.models.approval_workflow.approval_workflow_model import ApprovalWorkflow
from backend.repositories.approval_workflow.approval_workflow_repository import ApprovalWorkflowRepository
from datetime import datetime

class ApprovalWorkflowService:
    @staticmethod
    def submit_request(request_id: int, request_type: str) -> ApprovalWorkflow:
        workflow = ApprovalWorkflow(request_id=request_id, request_type=request_type, submitted_date=datetime.utcnow())
        ApprovalWorkflowRepository.save(workflow)
        return workflow

    @staticmethod
    def approve_request(request_id: int, approved_by: int) -> None:
        workflow = ApprovalWorkflowRepository.get_by_request_id(request_id)
        if workflow and workflow.approval_status == 'pending':
            workflow.approval_status = 'approved'
            workflow.approved_by = approved_by
            workflow.processed_date = datetime.utcnow()
            ApprovalWorkflowRepository.save(workflow)

    @staticmethod
    def reject_request(request_id: int, approved_by: int) -> None:
        workflow = ApprovalWorkflowRepository.get_by_request_id(request_id)
        if workflow and workflow.approval_status == 'pending':
            workflow.approval_status = 'rejected'
            workflow.approved_by = approved_by
            workflow.processed_date = datetime.utcnow()
            ApprovalWorkflowRepository.save(workflow)

# File 4: Approval Workflow Controller in controllers/approval_workflow/approval_workflow_controller.py