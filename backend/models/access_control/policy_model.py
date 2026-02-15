# Epic Title: Access Policies for Different Roles

from sqlalchemy import Column, Integer, String
from backend.app import db

class Policy(db.Model):
    __tablename__ = 'policies'

    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, nullable=False)
    service_name = Column(String(255), nullable=False)
    action = Column(String(50), nullable=False)

    def __init__(self, role_id: int, service_name: str, action: str):
        self.role_id = role_id
        self.service_name = service_name
        self.action = action


# File 2: Policy Repository in `repositories/access_control/policy_repository.py`