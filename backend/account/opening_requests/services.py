# Epic Title: Streamline Account Opening Requests

import logging
from typing import Optional
from backend.account.opening_requests.models import AccountOpeningRequest
from backend.authentication.models.user import User

logger = logging.getLogger(__name__)

class AccountOpeningService:
    def __init__(self, db):
        self.db = db
    
    def create_opening_request(self, user_id: int, account_type: str, initial_deposit: float) -> AccountOpeningRequest:
        opening_request = AccountOpeningRequest(user_id=user_id, account_type=account_type, initial_deposit=initial_deposit)
        self.db.session.add(opening_request)
        self.db.session.commit()
        logger.info(f"Created account opening request for user_id: {user_id}, account_type: {account_type}")
        return opening_request

    def get_opening_request(self, request_id: int) -> Optional[AccountOpeningRequest]:
        return AccountOpeningRequest.query.get(request_id)

    def update_request_status(self, request_id: int, status: str) -> bool:
        opening_request = self.get_opening_request(request_id)
        if opening_request:
            opening_request.status = status
            self.db.session.commit()
            logger.info(f"Updated account opening request {request_id} status to {status}")
            return True
        return False