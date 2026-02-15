# Epic Title: Account Opening and Service Modifications

from backend.models.accounts.approval_workflow_model import ApprovalWorkflow

class ApprovalWorkflowRepository:
    @staticmethod
    def save(workflow: ApprovalWorkflow) -> None:
        db.session.add(workflow)
        db.session.commit()

    @staticmethod
    def update(workflow: ApprovalWorkflow) -> None:
        db.session.commit()

    @staticmethod
    def find_by_request_id(request_id: int) -> ApprovalWorkflow:
        return ApprovalWorkflow.query.filter_by(request_id=request_id).first()


# File 3: ApprovalWorkflowService to Handle Workflow Logic in services/accounts/approval_workflow_service.py