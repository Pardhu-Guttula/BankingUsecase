# Epic Title: Service Modification Requests

import logging
from typing import Optional
from backend.account.service_modifications.models import ServiceModificationRequest
from backend.authentication.models.user import User

logger = logging.getLogger(__name__)

class ServiceModificationService:
    def __init__(self, db):
        self.db = db
    
    def create_modification_request(self, user_id: int, service_type: str, new_value: str) -> ServiceModificationRequest:
        modification_request = ServiceModificationRequest(user_id=user_id, service_type=service_type, new_value=new_value)
        self.db.session.add(modification_request)
        self.db.session.commit()
        logger.info(f"Created service modification request for user_id: {user_id}, service_type: {service_type}")
        return modification_request

    def get_modification_request(self, request_id: int) -> Optional[ServiceModificationRequest]:
        return ServiceModificationRequest.query.get(request_id)

    def update_request_status(self, request_id: int, status: str) -> bool:
        modification_request = self.get_modification_request(request_id)
        if modification_request:
            modification_request.status = status
            self.db.session.commit()
            logger.info(f"Updated service modification request {request_id} status to {status}")
            return True
        return False