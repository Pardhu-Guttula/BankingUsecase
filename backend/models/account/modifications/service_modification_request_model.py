# Epic Title: Service Modification Requests

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from backend.app import db
from datetime import datetime

class ServiceModificationRequest(db.Model):
    __tablename__ = 'service_modification_requests'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    modified_service = Column(String(100), nullable=False)
    status = Column(String(50), nullable=False, default='Pending')
    submission_date = Column(DateTime, default=datetime.utcnow)
    approved = Column(Boolean, default=False)

    def __init__(self, user_id: int, account_id: int, modified_service: str):
        self.user_id = user_id
        self.account_id = account_id
        self.modified_service = modified_service
        self.status = 'Pending'
        self.submission_date = datetime.utcnow()
        self.approved = False


# File 2: Service Modification Request Repository in repositories/account/modifications/service_modification_request_repository.py