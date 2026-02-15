# Epic Title: Account Opening and Service Modifications

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from backend.app import db
from datetime import datetime

class ServiceModificationRequest(db.Model):
    __tablename__ = 'service_modification_requests'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    request_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    service_type = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False, default='pending')

    def __init__(self, user_id: int, account_id: int, service_type: str, status: str = 'pending'):
        self.user_id = user_id
        self.account_id = account_id
        self.service_type = service_type
        self.status = status

# File 2: Service Modification Request Repository in repositories/account/modifications/service_modification_request_repository.py