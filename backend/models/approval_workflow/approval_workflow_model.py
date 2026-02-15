# Epic Title: Account Opening and Service Modifications

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from backend.app import db
from datetime import datetime

class ApprovalWorkflow(db.Model):
    __tablename__ = 'approval_workflows'

    id = Column(Integer, primary_key=True)
    request_id = Column(Integer, nullable=False)
    request_type = Column(String(50), nullable=False)
    submitted_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    approval_status = Column(String(50), nullable=False, default='pending')
    approved_by = Column(Integer, ForeignKey('users.id'))
    processed_date = Column(DateTime)

    def __init__(self, request_id: int, request_type: str, submitted_date: datetime, approval_status: str = 'pending', approved_by: int = None, processed_date: datetime = None):
        self.request_id = request_id
        self.request_type = request_type
        self.submitted_date = submitted_date
        self.approval_status = approval_status
        self.approved_by = approved_by
        self.processed_date = processed_date

# File 2: Approval Workflow Repository in repositories/approval_workflow/approval_workflow_repository.py