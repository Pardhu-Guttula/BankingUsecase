# Epic Title: Account Opening and Service Modifications

from backend.models.approval_workflow.approval_request_model import ApprovalRequest
from backend.app import db

class ApprovalRepository:
    @staticmethod
    def save(approval_request: ApprovalRequest) -> None:
        db.session.add(approval_request)
        db.session.commit()

    @staticmethod
    def find_by_id(approval_request_id: int) -> ApprovalRequest:
        return ApprovalRequest.query.get(approval_request_id)
        
    @staticmethod
    def find_pending_requests() -> list[ApprovalRequest]:
        return ApprovalRequest.query.filter_by(status='pending').all()


# File 4: Approval Workflow Controller to Handle Routes in controllers/approval_workflow/approval_controller.py