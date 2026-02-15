# Epic Title: User Authentication and Security

from backend.models.authentication.user_model import User
from backend.app import db

class UserRepository:
    @staticmethod
    def save(user: User) -> None:
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def find_by_id(user_id: int) -> User:
        return User.query.get(user_id)

    @staticmethod
    def find_by_username(username: str) -> User:
        return User.query.filter_by(username=username).first()

    @staticmethod
    def update_last_activity(user: User) -> None:
        user.last_activity = datetime.utcnow()
        db.session.commit()

    @staticmethod
    def is_session_expired(user: User, timeout: int) -> bool:
        return datetime.utcnow() - user.last_activity > timedelta(minutes=timeout)


# File 3: Update Authentication Service to Use Encryption in auth/services/authentication_service.py