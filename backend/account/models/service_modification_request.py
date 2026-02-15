# Epic Title: Service Modification Requests

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class ServiceModificationRequest(Base):
    __tablename__ = 'service_modification_requests'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    service_name = Column(String(50), nullable=False)
    status = Column(String(20), default='pending')

    user = relationship('User', back_populates='service_modification_requests')

    def __repr__(self) -> str:
        return f"<ServiceModificationRequest(user_id='{self.user_id}', service_name='{self.service_name}', status='{self.status}')>"



# File 2: Updated User Model in account/models/user.py