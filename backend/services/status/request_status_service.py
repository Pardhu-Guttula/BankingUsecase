# Epic Title: Real-time Status Updates

from backend.repositories.status.request_status_repository import RequestStatusRepository
from backend.models.status.request_status_model import RequestStatus
from datetime import datetime

class RequestStatusService:
    @staticmethod
    def create_status(request_id: int, status: str, request_type: str) -> None:
        request_status = RequestStatus(request_id=request_id, status=status, request_type=request_type)
        RequestStatusRepository.save(request_status)

    @staticmethod
    def update_status(request_id: int, status: str) -> None:
        request_status = RequestStatus.query.filter_by(request_id=request_id).order_by(RequestStatus.updated_at.desc()).first()
        if request_status:
            request_status.status = status
            request_status.updated_at = datetime.utcnow()
            RequestStatusRepository.update(request_status)

    @staticmethod
    def get_statuses_by_request(request_id: int) -> list:
        return RequestStatusRepository.find_by_request_id(request_id)


# File 4: Status Update Controller in controllers/status/request_status_controller.py