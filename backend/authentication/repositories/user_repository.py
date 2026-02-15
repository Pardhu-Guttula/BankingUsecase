# Epic Title: User Authentication and Security

from backend.models.authentication.user_model import User
from backend.app import db
from werkzeug.security import check_password_hash

class UserRepository:
    @staticmethod
    def get_user_by_username(username: str) -> User:
        return User.query.filter_by(username=username).first()

    @staticmethod
    def verify_password(user: User, password: str) -> bool:
        return check_password_hash(user.password_hash, password)

    @staticmethod
    def save(user: User) -> None:
        db.session.add(user)
        db.session.commit()


# File 4: Two-Factor Authentication Repository in authentication/repositories/two_factor_repository.py