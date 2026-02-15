# Epic Title: Role-based Access Control

from sqlalchemy import Column, Integer, String
from backend.app import db

class Role(db.Model):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255), nullable=True)

    def __init__(self, name: str, description: str = None):
        self.name = name
        self.description = description


# File 2: User-Role Association Model in models/access_control/user_role_model.py