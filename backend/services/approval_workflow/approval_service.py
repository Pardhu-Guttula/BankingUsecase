# Epic Title: Account Opening and Service Modifications

from backend.models.approval_workflow.approval_request_model import ApprovalRequest
from backend.repositories.approval_workflow.approval_repository import ApprovalRepository
from backend.app import db

class ApprovalService:
    @staticmethod
    def submit_approval_request(user_id: int, request_type: str, request_id: int) -> bool:
        try:
            approval_request = ApprovalRequest(user_id=user_id, request_type=request_type, request_id=request_id)
            ApprovalRepository.save(approval_request)
            return True
        except Exception as e:
            db.session.rollback()
            return False

    @staticmethod
    def process_approval_request(approval_request_id: int, status: str) -> bool:
        try:
            approval_request = ApprovalRepository.find_by_id(approval_request_id)
            if approval_request:
                approval_request.status = status
                db.session.commit()
                # Implement further processing logic based on the status and request_type
                return True
            return False
        except Exception as e:
            db.session.rollback()
            return False


# File 3: Approval Workflow Repository to Manage Approval Requests in repositories/approval_workflow/approval_repository.py