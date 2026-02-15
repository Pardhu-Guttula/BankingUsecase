# Epic Title: Real-time Status Updates and Notifications

from backend.repositories.notifications.status_update_repository import StatusUpdateRepository
from backend.models.notifications.status_update_model import StatusUpdate

class StatusUpdateService:
    @staticmethod
    def create_status_update(user_id: int, request_id: int, update_message: str, status: str) -> StatusUpdate:
        update = StatusUpdate(user_id, request_id, update_message, status)
        StatusUpdateRepository.save(update)
        return update

    @staticmethod
    def get_status_updates(user_id: int) -> list[StatusUpdate]:
        return StatusUpdateRepository.find_by_user_id(user_id)


# File 5: Dashboard Controller Update to Display Real-Time Status Updates in controllers/dashboard/dashboard_controller.py