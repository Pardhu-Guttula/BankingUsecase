# Epic Title: Role-based Access Control

from sqlalchemy import Column, Integer, String
from backend.app import db

class Policy(db.Model):
    __tablename__ = 'policies'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255), nullable=True)

    def __init__(self, name: str, description: str = None):
        self.name = name
        self.description = description


# File 2: Role-Policy Association Model in models/access_control/role_policy_model.py