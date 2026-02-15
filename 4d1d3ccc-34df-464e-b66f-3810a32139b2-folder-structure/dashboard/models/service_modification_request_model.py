# Epic Title: Service Modification Requests

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from backend.app import db

class ServiceModificationRequest(db.Model):
    __tablename__ = 'service_modification_requests'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    service = Column(String(100), nullable=False)
    status = Column(String(50), default='pending', nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref='service_modification_requests')
    account = db.relationship('Account', backref='service_modification_requests')

    def __init__(self, user_id: int, account_id: int, service: str):
        self.user_id = user_id
        self.account_id = account_id
        self.service = service


# File 2: Service Modification Request Repository for Database Operations in dashboard/repositories/service_modification_request_repository.py