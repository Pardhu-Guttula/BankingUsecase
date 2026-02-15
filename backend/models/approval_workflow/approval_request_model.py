# Epic Title: Account Opening and Service Modifications

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from backend.app import db

class ApprovalRequest(db.Model):
    __tablename__ = 'approval_requests'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    request_type = Column(String(50), nullable=False)  # e.g., 'account_opening', 'service_modification'
    request_id = Column(Integer, nullable=False)
    status = Column(String(20), default='pending', nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    def __init__(self, user_id: int, request_type: str, request_id: int, status: str='pending'):
        self.user_id = user_id
        self.request_type = request_type
        self.request_id = request_id
        self.status = status


# File 2: Approval Workflow Service to Handle Approval Logic in services/approval_workflow/approval_service.py