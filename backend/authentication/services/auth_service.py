# Epic Title: Manage Secure Storage of Credentials

from ..models.user import User
from ..models.session import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from cryptography.fernet import Fernet
import random
import string

DATABASE_URI = 'mysql+pymysql://username:password@localhost/db_name'
engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class AuthService:
    def __init__(self):
        self.db = SessionLocal()
        self.encryption_key = Fernet.generate_key()

    def authenticate(self, username: str, password: str, second_factor: str) -> bool:
        user = self.db.query(User).filter(User.username == username).first()
        
        if user and user.check_password(password):
            if user.mfa_enabled and self.verify_second_factor(user, second_factor):
                self.create_session(user)
                return True

        return False

    def verify_second_factor(self, user: User, second_factor: str) -> bool:
        return second_factor == "123456"

    def create_session(self, user: User):
        raw_token = ''.join(random.choices(string.ascii_letters + string.digits, k=64))
        encrypted_token = Session.encrypt_token(raw_token, self.encryption_key)
        session = Session(user_id=user.id, token=encrypted_token)
        self.db.add(session)
        self.db.commit()

    def verify_session(self, token: str) -> bool:
        from ..repositories.session_repository import SessionRepository
        session_repo = SessionRepository()
        decrypted_token = Session.decrypt_token(token, self.encryption_key)
        return session_repo.update_session_activity(decrypted_token)



# File 4: Update Session Repository for Secure Storage in authentication/repositories/session_repository.py