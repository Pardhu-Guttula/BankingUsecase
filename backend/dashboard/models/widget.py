# Epic Title: Customizable Widgets

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Widget(Base):
    __tablename__ = 'widgets'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    widget_type = Column(String(50), nullable=False)
    settings = Column(String(255))  # JSON or serialized string to store widget settings

    user = relationship('User', back_populates='widgets')

    def __repr__(self) -> str:
        return f"<Widget(user_id='{self.user_id}', widget_type='{self.widget_type}', settings='{self.settings}')>"



# File 2: Updated User Model for Widget Relationships in dashboard/models/user.py