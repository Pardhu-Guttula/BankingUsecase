# Epic Title: Account Opening and Service Modifications

from backend.models.approval_workflow.request_model import Request
from backend.app import db

class RequestRepository:
    @staticmethod
    def save(request: Request) -> None:
        db.session.add(request)
        db.session.commit()

    @staticmethod
    def update(request: Request) -> None:
        db.session.commit()

    @staticmethod
    def find_by_user_id(user_id: int) -> list[Request]:
        return Request.query.filter_by(user_id=user_id).all()

    @staticmethod
    def find_by_id(request_id: int) -> Request:
        return Request.query.filter_by(id=request_id).first()


# File 3: Approval Service to Handle Approval and Processing of Requests in approval_workflow/services/approval_service.py