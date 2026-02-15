# Epic Title: Role-based Access Control

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app import db

class Policy(db.Model):
    __tablename__ = 'policies'

    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)
    service_name = Column(String(50), nullable=False)
    access_level = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    role = relationship("Role", back_populates="policies")

    def __init__(self, role_id: int, service_name: str, access_level: str):
        self.role_id = role_id
        self.service_name = service_name
        self.access_level = access_level


# File 2: Update Role Model to Include Policies Relationship in models/access_control/role_model.py