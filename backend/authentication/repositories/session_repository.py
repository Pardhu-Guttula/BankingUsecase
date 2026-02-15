# Epic Title: Manage Secure Storage of Credentials

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from ..models.session import Session
from datetime import datetime
from typing import Optional

DATABASE_URI = 'mysql+pymysql://username:password@localhost/db_name'
engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class SessionRepository:
    def __init__(self):
        self.db = SessionLocal()

    def get_session_by_token(self, token: str) -> Optional[Session]:
        return self.db.query(Session).filter(Session.token == token).first()

    def update_session_activity(self, token: str):
        session = self.get_session_by_token(token)
        if session:
            current_time = datetime.utcnow()
            if session.is_expired(current_time):
                self.db.delete(session)
                self.db.commit()
                return False
            else:
                session.update_activity(current_time)
                self.db.commit()
                return True
        return False

    def delete_session_by_token(self, token: str):
        session = self.get_session_by_token(token)
        if session:
            self.db.delete(session)
            self.db.commit()



# File 5: Database Schema Update for Secure Storage in database/users.sql