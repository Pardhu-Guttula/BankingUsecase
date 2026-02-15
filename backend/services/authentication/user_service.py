# Epic Title: User Authentication and Security

from backend.models.authentication.user_model import User
from backend.repositories.authentication.user_repository import UserRepository
import bcrypt

class UserService:
    @staticmethod
    def hash_password(password: str) -> str:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    @staticmethod
    def verify_password(password: str, password_hash: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))

    @staticmethod
    def create_user(username: str, email: str, password: str) -> User:
        password_hash = UserService.hash_password(password)
        user = User(username=username, email=email, password_hash=password_hash)
        UserRepository.save(user)
        return user

# File 4: User Controller in controllers/authentication/user_controller.py