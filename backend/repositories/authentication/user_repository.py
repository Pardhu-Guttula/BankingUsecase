# Epic Title: User Authentication and Security

from backend.models.authentication.user_model import User

class UserRepository:
    @staticmethod
    def find_by_username(username: str) -> User:
        return User.query.filter_by(username=username).first()

    @staticmethod
    def find_by_id(user_id: int) -> User:
        return User.query.get(user_id)

    @staticmethod
    def save(user: User) -> None:
        db.session.add(user)
        db.session.commit()


# File 4: Authentication Controller for Handling Login Requests in controllers/authentication/authentication_controller.py