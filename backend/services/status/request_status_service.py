# Epic Title: Real-time Status Updates and Notifications

from backend.repositories.status.request_status_repository import RequestStatusRepository
from backend.models.status.request_status_model import RequestStatus
from backend.services.notifications.email_notification_service import EmailNotificationService
from backend.models.authentication.user_model import User

class RequestStatusService:
    @staticmethod
    def create_status(request_id: int, status: str, user_id: int) -> RequestStatus:
        request_status = RequestStatus(request_id=request_id, status=status, user_id=user_id)
        RequestStatusRepository.save(request_status)
        RequestStatusService.notify_user(request_status)
        return request_status

    @staticmethod
    def update_status(request_id: int, status: str, user_id: int) -> RequestStatus:
        request_status = RequestStatus.query.filter_by(request_id=request_id, user_id=user_id).first()
        if request_status:
            request_status.status = status
            RequestStatusRepository.update(request_status)
            RequestStatusService.notify_user(request_status)
        return request_status

    @staticmethod
    def notify_user(request_status: RequestStatus) -> None:
        user = User.query.get(request_status.user_id)
        if user:
            subject = f"Update on Request {request_status.request_id}"
            content = f"Your request with ID {request_status.request_id} has a new status: {request_status.status}"
            EmailNotificationService.create_notification(
                request_id=request_status.request_id,
                user_id=user.id,
                email=user.email,
                subject=subject,
                content=content
            )
            email_notification = EmailNotificationService.create_notification(
                request_id=request_status.request_id,
                user_id=user.id,
                email=user.email,
                subject=subject,
                content=content
            )
            EmailNotificationService.send_email(email_notification)


# File 6: Update Main App to Initialize Flask-Mail in app.py