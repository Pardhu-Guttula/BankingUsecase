# Epic Title: Approval and Processing Workflows

import logging
from datetime import datetime
from typing import Optional
from backend.approval_workflow.models import ApprovalWorkflow

logger = logging.getLogger(__name__)

class ApprovalService:
    def __init__(self, db):
        self.db = db
    
    def initiate_approval(self, request_id: int, request_type: str) -> ApprovalWorkflow:
        workflow = ApprovalWorkflow(request_id=request_id, request_type=request_type)
        self.db.session.add(workflow)
        self.db.session.commit()
        logger.info(f"Initiated approval workflow for {request_type} request_id: {request_id}")
        return workflow

    def get_approval_status(self, request_id: int, request_type: str) -> Optional[ApprovalWorkflow]:
        return ApprovalWorkflow.query.filter_by(request_id=request_id, request_type=request_type).first()

    def update_approval_status(self, workflow_id: int, status: str) -> bool:
        workflow = ApprovalWorkflow.query.get(workflow_id)
        if workflow:
            workflow.status = status
            workflow.processed_at = datetime.utcnow() if status in ['approved', 'rejected'] else None
            self.db.session.commit()
            logger.info(f"Updated approval workflow {workflow_id} status to {status}")
            return True
        return False