# Epic Title: Account Opening and Service Modifications

from backend.models.approval_workflow.approval_model import ApprovalWorkflow
from backend.app import db

class ApprovalWorkflowRepository:
    @staticmethod
    def save(approval_workflow: ApprovalWorkflow) -> None:
        db.session.add(approval_workflow)
        db.session.commit()

    @staticmethod
    def get_approval_by_request_id(request_id: int, request_type: str) -> ApprovalWorkflow:
        return ApprovalWorkflow.query.filter_by(request_id=request_id, request_type=request_type).first()

    @staticmethod
    def update(approval_workflow: ApprovalWorkflow) -> None:
        db.session.commit()

    @staticmethod
    def delete(approval_workflow: ApprovalWorkflow) -> None:
        db.session.delete(approval_workflow)
        db.session.commit()

# File 3: Approval Workflow Service to Handle Business Logic in services/approval_workflow/approval_workflow_service.py