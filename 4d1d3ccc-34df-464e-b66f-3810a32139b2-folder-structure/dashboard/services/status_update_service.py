# Epic Title: Real-time Status Updates and Notifications

from dashboard.repositories.status_update_repository import StatusUpdateRepository
from dashboard.models.status_update_model import StatusUpdate

class StatusUpdateService:
    @staticmethod
    def create_status_update(request_id: int, status: str) -> StatusUpdate:
        status_update = StatusUpdate(request_id, status)
        StatusUpdateRepository.save(status_update)
        return status_update

    @staticmethod
    def get_request_status_updates(request_id: int) -> list:
        updates = StatusUpdateRepository.get_updates_by_request_id(request_id)
        return [{
            "id": update.id,
            "status": update.status,
            "updated_at": update.updated_at
        } for update in updates]


# File 4: Status Update Controller for Handling Requests in dashboard/controllers/status_update_controller.py