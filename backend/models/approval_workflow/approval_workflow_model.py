# Epic Title: Approval and Processing Workflows

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from backend.app import db
from datetime import datetime

class ApprovalWorkflow(db.Model):
    __tablename__ = 'approval_workflows'

    id = Column(Integer, primary_key=True)
    request_id = Column(Integer, nullable=False)
    request_type = Column(String(50), nullable=False)
    approver_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    status = Column(String(50), nullable=False, default='Pending')
    approval_date = Column(DateTime, nullable=True)
    comments = Column(String(255), nullable=True)

    def __init__(self, request_id: int, request_type: str, approver_id: int):
        self.request_id = request_id
        self.request_type = request_type
        self.approver_id = approver_id
        self.status = 'Pending'
        self.approval_date = None
        self.comments = None


# File 2: Approval Workflow Repository in repositories/approval_workflow/approval_workflow_repository.py