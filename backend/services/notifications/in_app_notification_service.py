# Epic Title: Real-time Status Updates and Notifications

from backend.repositories.notifications.in_app_notification_repository import InAppNotificationRepository
from backend.models.notifications.in_app_notification_model import InAppNotification

class InAppNotificationService:
    @staticmethod
    def create_notification(request_id: int, user_id: int, message: str) -> InAppNotification:
        in_app_notification = InAppNotification(request_id=request_id, user_id=user_id, message=message)
        InAppNotificationRepository.save(in_app_notification)
        return in_app_notification

    @staticmethod
    def mark_notification_as_read(notification_id: int) -> None:
        in_app_notification = InAppNotification.query.get(notification_id)
        if in_app_notification:
            InAppNotificationRepository.mark_as_read(in_app_notification)


# File 5: Integrate In-App Notifications with Request Status Service in services/status/request_status_service.py (Update)