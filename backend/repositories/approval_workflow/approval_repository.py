# Epic Title: Account Opening and Service Modifications

from backend.models.approval_workflow.request_approval_model import RequestApproval
from backend.app import db

class ApprovalRepository:
    @staticmethod
    def get_pending_approvals() -> list[RequestApproval]:
        return RequestApproval.query.filter_by(status='Pending').all()

    @staticmethod
    def save(request_approval: RequestApproval) -> None:
        db.session.add(request_approval)
        db.session.commit()

    @staticmethod
    def update(request_approval: RequestApproval) -> None:
        db.session.commit()


# File 4: Approval Service Layer in services/approval_workflow/approval_service.py