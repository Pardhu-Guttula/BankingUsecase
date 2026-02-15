# Epic Title: Approval and Processing Workflows

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from backend.app import db

class ApprovalWorkflow(db.Model):
    __tablename__ = 'approval_workflows'

    id = Column(Integer, primary_key=True)
    request_type = Column(String(50), nullable=False)
    request_id = Column(Integer, nullable=False)
    approver_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    status = Column(String(50), default='pending', nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    approver = db.relationship('User', backref='approval_workflows')

    def __init__(self, request_type: str, request_id: int, approver_id: int):
        self.request_type = request_type
        self.request_id = request_id
        self.approver_id = approver_id


# File 2: Approval Workflow Repository for Database Operations in dashboard/repositories/approval_workflow_repository.py