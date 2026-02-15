# Epic Title: Approval and Processing Workflows

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from ..models.approval_workflow import ApprovalWorkflow

DATABASE_URI = 'mysql+pymysql://username:password@localhost/db_name'
engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class ApprovalWorkflowService:
    def __init__(self):
        self.db = SessionLocal()

    def approve_request(self, workflow_id: int, approver: str) -> bool:
        workflow_entry = self.db.query(ApprovalWorkflow).filter(ApprovalWorkflow.id == workflow_id).first()
        if workflow_entry:
            workflow_entry.status = 'approved'
            workflow_entry.approver = approver
            self.db.commit()
            return True
        return False

    def reject_request(self, workflow_id: int, approver: str) -> bool:
        workflow_entry = self.db.query(ApprovalWorkflow).filter(ApprovalWorkflow.id == workflow_id).first()
        if workflow_entry:
            workflow_entry.status = 'rejected'
            workflow_entry.approver = approver
            self.db.commit()
            return True
        return False

    def pending_requests(self):
        return self.db.query(ApprovalWorkflow).filter(ApprovalWorkflow.status == 'pending').all()


# File 5: Approval Workflow Controller in accesscontrol/controllers/approval_workflow_controller.py