# Epic Title: Implement Secure Login Mechanism

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Session(Base):
    __tablename__ = 'sessions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    token = Column(String(64), unique=True, nullable=False)
    created_at = Column(DateTime, default=func.now())

    # Establish relationship with User
    user = relationship('User', back_populates='sessions')

    def __repr__(self) -> str:
        return f"<Session(user_id='{self.user_id}', token='{self.token}', created_at='{self.created_at}')>"



# File 3: User and Session Relationship in authentication/models/user.py