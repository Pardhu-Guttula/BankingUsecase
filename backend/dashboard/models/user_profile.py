# Epic Title: Develop a User-Friendly Dashboard

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class UserProfile(Base):
    __tablename__ = 'user_profiles'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    display_name = Column(String(100), nullable=False)
    preferences = Column(String(500))  # JSON or serialized string to store user preferences
    
    user = relationship('User', back_populates='profile')

    def __repr__(self) -> str:
        return f"<UserProfile(user_id='{self.user_id}', display_name='{self.display_name}', preferences='{self.preferences}')>"



# File 2: Account Model in account/models/account.py