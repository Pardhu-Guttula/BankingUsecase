# Epic Title: Role-based Access Control

from backend.models.access_control.user_model import User
from backend.app import db

class UserRepository:
    @staticmethod
    def save(user: User) -> None:
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def find_by_username(username: str) -> User | None:
        return User.query.filter_by(username=username).first()

# File 7: Register Role Controller Blueprint in app.py (Already Exists, Modified)