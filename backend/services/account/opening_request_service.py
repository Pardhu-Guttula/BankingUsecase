# Epic Title: Account Opening and Service Modifications

from backend.models.account.opening_request_model import OpeningRequest
from backend.repositories.account.opening_request_repository import OpeningRequestRepository

class OpeningRequestService:
    @staticmethod
    def create_opening_request(user_id: int, account_type: str) -> OpeningRequest:
        opening_request = OpeningRequest(user_id=user_id, account_type=account_type)
        OpeningRequestRepository.save(opening_request)
        return opening_request

    @staticmethod
    def get_user_opening_requests(user_id: int) -> list[OpeningRequest]:
        return OpeningRequestRepository.get_requests_by_user_id(user_id)

    @staticmethod
    def update_opening_request_status(request_id: int, status: str) -> None:
        opening_request = OpeningRequest.query.get(request_id)
        if opening_request:
            opening_request.status = status
            OpeningRequestRepository.update(opening_request)

# File 4: Account Opening Controller to Handle Form Submission in account/controllers/opening/account_opening_controller.py