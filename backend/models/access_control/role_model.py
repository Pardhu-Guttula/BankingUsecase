# Epic Title: Role-based Access Control

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.app import db

class Role(db.Model):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255), nullable=True)

    users = relationship('User', back_populates='role')

    def __init__(self, name: str, description: str = ''):
        self.name = name
        self.description = description


# File 2: Update User Model to Include Role Relationship in models/authentication/user_model.py