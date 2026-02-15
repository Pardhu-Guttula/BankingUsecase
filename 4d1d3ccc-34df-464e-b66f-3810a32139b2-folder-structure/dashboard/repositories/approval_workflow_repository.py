# Epic Title: Approval and Processing Workflows

from dashboard.models.approval_workflow_model import ApprovalWorkflow
from backend.app import db

class ApprovalWorkflowRepository:
    @staticmethod
    def save(workflow: ApprovalWorkflow) -> None:
        db.session.add(workflow)
        db.session.commit()

    @staticmethod
    def get_workflow_by_request(request_type: str, request_id: int) -> ApprovalWorkflow:
        return ApprovalWorkflow.query.filter_by(request_type=request_type, request_id=request_id).first()

    @staticmethod
    def update_status(workflow: ApprovalWorkflow, status: str) -> None:
        workflow.status = status
        db.session.commit()


# File 3: Approval Workflow Service for Business Logic in dashboard/services/approval_workflow_service.py