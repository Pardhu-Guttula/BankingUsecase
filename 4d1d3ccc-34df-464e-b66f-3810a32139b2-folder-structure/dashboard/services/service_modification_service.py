# Epic Title: Service Modification Requests

from dashboard.repositories.service_modification_request_repository import ServiceModificationRequestRepository
from dashboard.models.service_modification_request_model import ServiceModificationRequest

class ServiceModificationService:
    @staticmethod
    def request_service_modification(user_id: int, account_id: int, service: str) -> ServiceModificationRequest:
        request = ServiceModificationRequest(user_id, account_id, service)
        ServiceModificationRequestRepository.save(request)
        return request

    @staticmethod
    def get_user_requests(user_id: int) -> list:
        requests = ServiceModificationRequestRepository.get_requests_by_user_id(user_id)
        return [{
            "id": request.id,
            "account_id": request.account_id,
            "service": request.service,
            "status": request.status,
            "created_at": request.created_at
        } for request in requests]


# File 4: Service Modification Controller for Handling Requests in dashboard/controllers/service_modification_controller.py