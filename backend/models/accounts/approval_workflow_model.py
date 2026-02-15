# Epic Title: Account Opening and Service Modifications

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app import db

class ApprovalWorkflow(db.Model):
    __tablename__ = 'approval_workflows'

    id = Column(Integer, primary_key=True)
    request_id = Column(Integer, nullable=False, unique=True)
    request_type = Column(String(50), nullable=False)
    status = Column(String(20), nullable=False, default='pending')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    def __init__(self, request_id: int, request_type: str, status: str = 'pending'):
        self.request_id = request_id
        self.request_type = request_type
        self.status = status


# File 2: Approval Workflow Repository in repositories/accounts/approval_workflow_repository.py