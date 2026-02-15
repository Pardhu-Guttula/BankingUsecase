# Epic Title: Role-based Access Control

from sqlalchemy import Column, Integer, String, ForeignKey
from backend.app import db

class Policy(db.Model):
    __tablename__ = 'policies'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)
    action = Column(String(255), nullable=False)

    def __init__(self, name: str, role_id: int, action: str):
        self.name = name
        self.role_id = role_id
        self.action = action

# File 2: Policy Repository in repositories/access_control/policy_repository.py