# Epic Title: Service Modification Requests

from backend.repositories.account.modifications.service_modification_request_repository import ServiceModificationRequestRepository
from backend.models.account.modifications.service_modification_request_model import ServiceModificationRequest

class ServiceModificationRequestService:
    @staticmethod
    def create_request(user_id: int, account_id: int, modified_service: str) -> None:
        request = ServiceModificationRequest(user_id=user_id, account_id=account_id, modified_service=modified_service)
        ServiceModificationRequestRepository.save(request)

    @staticmethod
    def get_user_requests(user_id: int) -> list:
        return ServiceModificationRequestRepository.find_by_user_id(user_id)


# File 4: Service Modification Request Controller in controllers/account/modifications/service_modification_request_controller.py