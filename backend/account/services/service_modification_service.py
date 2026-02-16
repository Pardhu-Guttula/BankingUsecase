# Epic Title: Account Opening and Service Modifications

import logging
from flask_sqlalchemy import SQLAlchemy
from backend.account.models.service_modification import ServiceModificationRequest

logger = logging.getLogger(__name__)

class ServiceModificationService:
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def create_modification_request(self, user_id: int, account_id: int, service_name: str, new_value: str) -> ServiceModificationRequest:
        modification_request = ServiceModificationRequest(user_id=user_id, account_id=account_id, service_name=service_name, new_value=new_value)
        self.db.session.add(modification_request)
        self.db.session.commit()
        logger.debug(f"Created service modification request {modification_request.id} for user {user_id}")
        return modification_request

    def get_modification_requests_for_user(self, user_id: int) -> list[ServiceModificationRequest]:
        logger.debug(f"Fetching service modification requests for user {user_id}")
        return ServiceModificationRequest.query.filter_by(user_id=user_id).all()

    def validate_modification_request(self, modification_request: ServiceModificationRequest) -> bool:
        # Add your validation logic here
        return True

    def approve_modification_request(self, modification_request_id: int):
        modification_request = ServiceModificationRequest.query.get(modification_request_id)
        if modification_request and self.validate_modification_request(modification_request):
            modification_request.status = "Approved"
            self.db.session.commit()
            logger.debug(f"Approved service modification request {modification_request_id}")
            return modification_request
        else:
            logger.warn(f"Service modification request {modification_request_id} could not be approved.")
            raise ValueError("Invalid service modification request or failed validation.")