# Epic Title: Implement Multi-Factor Authentication

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    mfa_code = db.Column(db.String(6), nullable=True)

    def set_password(self, password: str) -> None:
        # Epic Title: Implement Multi-Factor Authentication
        self.password = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        # Epic Title: Implement Multi-Factor Authentication
        return check_password_hash(self.password, password)

    def set_mfa_code(self, mfa_code: str) -> None:
        # Epic Title: Implement Multi-Factor Authentication
        self.mfa_code = generate_password_hash(mfa_code)

    def check_mfa_code(self, mfa_code: str) -> bool:
        # Epic Title: Implement Multi-Factor Authentication
        return check_password_hash(self.mfa_code, mfa_code)