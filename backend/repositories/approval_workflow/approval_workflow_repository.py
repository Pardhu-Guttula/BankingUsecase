# Epic Title: Approval and Processing Workflows

from backend.models.approval_workflow.approval_workflow_model import ApprovalWorkflow
from backend.app import db

class ApprovalWorkflowRepository:
    @staticmethod
    def save(workflow: ApprovalWorkflow) -> None:
        db.session.add(workflow)
        db.session.commit()

    @staticmethod
    def update(workflow: ApprovalWorkflow) -> None:
        db.session.commit()

    @staticmethod
    def find_by_request_id(request_id: int, request_type: str) -> list[ApprovalWorkflow]:
        return ApprovalWorkflow.query.filter_by(request_id=request_id, request_type=request_type).all()


# File 3: Approval Workflow Service in services/approval_workflow/approval_workflow_service.py