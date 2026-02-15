# Epic Title: Real-time Status Updates and Notifications

from backend.models.status.request_status_model import RequestStatus
from backend.repositories.status.request_status_repository import RequestStatusRepository
from backend.services.notifications.email_notification_service import EmailNotificationService
from datetime import datetime

class RequestStatusService:
    @staticmethod
    def create_status(request_id: int, status: str, user_id: int, user_email: str) -> RequestStatus:
        status_obj = RequestStatus(request_id=request_id, status=status, user_id=user_id)
        RequestStatusRepository.save(status_obj)
        EmailNotificationService.send_email(
            subject="Request Created",
            recipients=[user_email],
            body=f"Your request with ID {request_id} has been created with status '{status}'."
        )
        return status_obj

    @staticmethod
    def update_status(request_id: int, new_status: str, user_email: str) -> None:
        status_obj = RequestStatusRepository.get_by_request_id(request_id)
        if status_obj:
            status_obj.status = new_status
            status_obj.last_updated = datetime.utcnow()
            RequestStatusRepository.save(status_obj)
            EmailNotificationService.send_email(
                subject="Request Status Updated",
                recipients=[user_email],
                body=f"Your request with ID {request_id} has been updated to status '{new_status}'."
            )

    @staticmethod
    def get_status_by_request_id(request_id: int) -> RequestStatus:
        return RequestStatusRepository.get_by_request_id(request_id)

    @staticmethod
    def get_statuses_by_user_id(user_id: int) -> list[RequestStatus]:
        return RequestStatusRepository.get_by_user_id(user_id)

# File 3: Request Status Controller Update in controllers/status/request_status_controller.py (Modified)