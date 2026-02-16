# Epic Title: Account Opening and Service Modifications

import logging
from flask_sqlalchemy import SQLAlchemy
from backend.approval_workflow.models import ApprovalRequest
from backend.account.models.opening_request import OpeningRequest
from backend.account.models.service_modification import ServiceModificationRequest

logger = logging.getLogger(__name__)

class ApprovalService:
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def initiate_approval(self, request_type: str, request_id: int) -> ApprovalRequest:
        approval_request = ApprovalRequest(request_type=request_type, request_id=request_id)
        self.db.session.add(approval_request)
        self.db.session.commit()
        logger.debug(f"Initiated approval request {approval_request.id} for {request_type} id={request_id}")
        return approval_request

    def approve_request(self, approval_request_id: int):
        approval_request = ApprovalRequest.query.get(approval_request_id)
        if approval_request:
            approval_request.status = "Approved"
            if approval_request.request_type == "AccountOpening":
                self._approve_account_opening(approval_request.request_id)
            elif approval_request.request_type == "ServiceModification":
                self._approve_service_modification(approval_request.request_id)
            self.db.session.commit()
            logger.debug(f"Approved request {approval_request_id} for {approval_request.request_type} id={approval_request.request_id}")
        else:
            logger.warn(f"Approval request {approval_request_id} not found or invalid.")

    def _approve_account_opening(self, request_id: int):
        opening_request = OpeningRequest.query.get(request_id)
        if not opening_request:
            logger.warn(f"Account opening request {request_id} not found.")
            raise ValueError("Account opening request not found")

        opening_request.status = "Approved"
        self.db.session.commit()
        logger.debug(f"Account opening request {request_id} approved.")

    def _approve_service_modification(self, request_id: int):
        modification_request = ServiceModificationRequest.query.get(request_id)
        if not modification_request:
            logger.warn(f"Service modification request {request_id} not found.")
            raise ValueError("Service modification request not found")

        modification_request.status = "Approved"
        self.db.session.commit()
        logger.debug(f"Service modification request {request_id} approved.")