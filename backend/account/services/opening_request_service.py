# Epic Title: Account Opening and Service Modifications

import logging
from flask_sqlalchemy import SQLAlchemy
from backend.account.models.opening_request import OpeningRequest

logger = logging.getLogger(__name__)

class OpeningRequestService:
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def create_opening_request(self, user_id: int, account_type: str, initial_deposit: float) -> OpeningRequest:
        opening_request = OpeningRequest(user_id=user_id, account_type=account_type, initial_deposit=initial_deposit)
        self.db.session.add(opening_request)
        self.db.session.commit()
        logger.debug(f"Created opening request {opening_request.id} for user {user_id}")
        return opening_request

    def get_opening_requests_for_user(self, user_id: int) -> list[OpeningRequest]:
        logger.debug(f"Fetching opening requests for user {user_id}")
        return OpeningRequest.query.filter_by(user_id=user_id).all()