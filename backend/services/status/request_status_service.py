# Epic Title: Real-time Status Updates and Notifications

from backend.repositories.status.request_status_repository import RequestStatusRepository
from backend.models.status.request_status_model import RequestStatus

class RequestStatusService:
    @staticmethod
    def create_status(request_id: int, status: str, user_id: int) -> RequestStatus:
        request_status = RequestStatus(request_id=request_id, status=status, user_id=user_id)
        RequestStatusRepository.save(request_status)
        return request_status

    @staticmethod
    def update_status(request_id: int, status: str, user_id: int) -> RequestStatus:
        request_status = RequestStatus.query.filter_by(request_id=request_id, user_id=user_id).first()
        if request_status:
            request_status.status = status
            RequestStatusRepository.update(request_status)
        return request_status


# File 5: Controller to Handle Real-Time Status Updates in status/controllers/request_status_controller.py