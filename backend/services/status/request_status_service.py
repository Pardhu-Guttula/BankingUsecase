# Epic Title: Real-time Status Updates and Notifications

from datetime import datetime
from backend.models.status.request_status_model import RequestStatus
from backend.repositories.status.request_status_repository import RequestStatusRepository
from backend.services.notifications.email_notification_service import EmailNotificationService
from backend.models.users.user_model import User
from backend.app import db

class RequestStatusService:
    @staticmethod
    def create_request_status(user_id: int, request_id: int, status: str) -> RequestStatus:
        request_status = RequestStatus(user_id=user_id, request_id=request_id, status=status)
        RequestStatusRepository.save(request_status)
        return request_status

    @staticmethod
    def get_request_status(request_id: int) -> RequestStatus:
        return RequestStatusRepository.get_status_by_request_id(request_id)

    @staticmethod
    def update_request_status(request_id: int, status: str) -> RequestStatus:
        request_status = RequestStatusRepository.get_status_by_request_id(request_id)
        if request_status.status != status:
            request_status.status = status
            request_status.updated_at = datetime.utcnow()
            RequestStatusRepository.update_status(request_status)
            
            user = db.session.query(User).filter(User.id == request_status.user_id).one()
            EmailNotificationService.send_email(
                user_id=user.id,
                email=user.email,
                subject="Request Status Update",
                content=f"Your request with ID {request_id} has been updated to {status}."
            )
            
        return request_status


# File 5: Real-time Status Controller Endpoint to Handle Status Updates in status/controllers/request_status_controller.py (Already Exists, Modified)