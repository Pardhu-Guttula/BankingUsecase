# Epic Title: Account Opening and Service Modifications

from backend.models.approval_workflow.approval_workflow_model import ApprovalWorkflow
from backend.app import db

class ApprovalWorkflowRepository:
    @staticmethod
    def save(workflow: ApprovalWorkflow) -> None:
        db.session.add(workflow)
        db.session.commit()

    @staticmethod
    def get_by_request_id(request_id: int) -> ApprovalWorkflow:
        return ApprovalWorkflow.query.filter_by(request_id=request_id).first()

    @staticmethod
    def get_all_pending() -> list[ApprovalWorkflow]:
        return ApprovalWorkflow.query.filter_by(approval_status='pending').all()

# File 3: Approval Workflow Service in services/approval_workflow/approval_workflow_service.py