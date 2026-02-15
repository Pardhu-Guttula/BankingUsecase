# Epic Title: Account Opening and Service Modifications

from backend.models.account.service_modification_request_model import ServiceModificationRequest
from backend.repositories.account.service_modification_request_repository import ServiceModificationRequestRepository

class ServiceModificationRequestService:
    @staticmethod
    def create_service_modification_request(user_id: int, service_type: str) -> ServiceModificationRequest:
        service_modification_request = ServiceModificationRequest(user_id=user_id, service_type=service_type)
        ServiceModificationRequestRepository.save(service_modification_request)
        return service_modification_request

    @staticmethod
    def get_user_service_modification_requests(user_id: int) -> list[ServiceModificationRequest]:
        return ServiceModificationRequestRepository.get_requests_by_user_id(user_id)

    @staticmethod
    def update_service_modification_request_status(request_id: int, status: str) -> None:
        service_modification_request = ServiceModificationRequest.query.get(request_id)
        if service_modification_request:
            service_modification_request.status = status
            ServiceModificationRequestRepository.update(service_modification_request)

# File 4: Service Modification Controller to Handle Form Submission in account/controllers/modifications/service_modification_controller.py