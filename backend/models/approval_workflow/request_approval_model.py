# Epic Title: Account Opening and Service Modifications

from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from backend.app import db
import datetime

class RequestApproval(db.Model):
    __tablename__ = 'request_approvals'

    id = Column(Integer, primary_key=True)
    request_id = Column(Integer, nullable=False)
    request_type = Column(String(50), nullable=False)
    status = Column(String(50), default='Pending', nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    approver_id = Column(Integer, ForeignKey('users.id'), nullable=True)

    approver = relationship('User', back_populates='approvals')

    def __init__(self, request_id: int, request_type: str, status: str = 'Pending', approver_id: int = None):
        self.request_id = request_id
        self.request_type = request_type
        self.status = status
        self.approver_id = approver_id

    
# File 2: Update User Model to Include Relationship with Approvals in models/authentication/user_model.py