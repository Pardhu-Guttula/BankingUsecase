# Epic Title: Streamline Account Opening Requests

from dashboard.repositories.account_opening_request_repository import AccountOpeningRequestRepository
from dashboard.models.account_opening_request_model import AccountOpeningRequest

class AccountOpeningService:
    @staticmethod
    def request_account_opening(user_id: int, account_type: str) -> AccountOpeningRequest:
        request = AccountOpeningRequest(user_id, account_type)
        AccountOpeningRequestRepository.save(request)
        return request

    @staticmethod
    def get_user_requests(user_id: int) -> list:
        requests = AccountOpeningRequestRepository.get_requests_by_user_id(user_id)
        return [{
            "id": request.id,
            "account_type": request.account_type,
            "status": request.status,
            "created_at": request.created_at
        } for request in requests]


# File 4: Account Opening Controller for Handling Requests in dashboard/controllers/account_opening_controller.py