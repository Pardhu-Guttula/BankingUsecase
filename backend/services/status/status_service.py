# Epic Title: Real-time Status Updates and Notifications

from backend.models.status.status_model import Status
from backend.repositories.status.status_repository import StatusRepository

class StatusService:
    @staticmethod
    def add_status_update(request_id: int, status: str) -> Status:
        status_update = Status(request_id=request_id, status=status)
        StatusRepository.save(status_update)
        return status_update

    @staticmethod
    def get_status_updates(request_id: int) -> list[Status]:
        return StatusRepository.get_status_by_request_id(request_id)

# File 4: Status Controller to Handle Real-time Status Updates in status/controllers/status_controller.py