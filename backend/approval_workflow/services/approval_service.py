# Epic Title: Account Opening and Service Modifications

from backend.models.approval_workflow.request_model import Request
from backend.approval_workflow.repositories.request_repository import RequestRepository
from backend.app import db

class ApprovalService:
    @staticmethod
    def approve_request(request_id: int) -> bool:
        try:
            request = RequestRepository.find_by_id(request_id)
            if request:
                request.status = 'Approved'
                RequestRepository.update(request)
                return True
            return False
        except Exception as e:
            db.session.rollback()
            return False

    @staticmethod
    def reject_request(request_id: int) -> bool:
        try:
            request = RequestRepository.find_by_id(request_id)
            if request:
                request.status = 'Rejected'
                RequestRepository.update(request)
                return True
            return False
        except Exception as e:
            db.session.rollback()
            return False

    @staticmethod
    def process_request(request_id: int) -> bool:
        try:
            request = RequestRepository.find_by_id(request_id)
            if request and request.status == 'Approved':
                # Add logic to process the request, e.g., opening account, modifying services, etc.
                request.status = 'Processed'
                RequestRepository.update(request)
                return True
            return False
        except Exception as e:
            db.session.rollback()
            return False


# File 4: Approval Controller for Managing Approval Workflow Endpoints in approval_workflow/controllers/approval_controller.py