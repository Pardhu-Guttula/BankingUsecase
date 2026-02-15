# Epic Title: Real-time Status Updates and Notifications

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.app import db

class Request(db.Model):
    __tablename__ = 'requests'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)

    statuses = relationship("Status", back_populates="request")

    def __init__(self, user_id: int, title: str, description: str = None):
        self.user_id = user_id
        self.title = title
        self.description = description


# File 6: Update Main App to Ensure Correct Initialization in app.py