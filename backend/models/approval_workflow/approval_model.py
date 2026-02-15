# Epic Title: Account Opening and Service Modifications

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app import db

class ApprovalRequest(db.Model):
    __tablename__ = 'approval_requests'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    request_type = Column(String(50), nullable=False)
    request_id = Column(Integer, nullable=False)
    status = Column(String(20), default='pending', nullable=False)
    submitted_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    reviewed_at = Column(DateTime, nullable=True)
    approved_by = Column(Integer, ForeignKey('users.id'), nullable=True)

    user = relationship('User', foreign_keys=[user_id], back_populates='approval_requests')
    approver = relationship('User', foreign_keys=[approved_by])

    def __init__(self, user_id: int, request_type: str, request_id: int, status: str = 'pending', submitted_at: DateTime = None, reviewed_at: DateTime = None, approved_by: int = None):
        self.user_id = user_id
        self.request_type = request_type
        self.request_id = request_id
        self.status = status
        if submitted_at is None:
            submitted_at = datetime.utcnow()
        self.submitted_at = submitted_at
        self.reviewed_at = reviewed_at
        self.approved_by = approved_by


# File 2: Approval Repository to Access Approval Data in repositories/approval_workflow/approval_repository.py