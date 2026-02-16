# Epic Title: User Authentication and Security

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username: str = db.Column(db.String(50), unique=True, nullable=False)
    email: str = db.Column(db.String(120), unique=True, nullable=False)
    password_hash: str = db.Column(db.String(128), nullable=False)
    mfa_enabled: bool = db.Column(db.Boolean, default=False)
    mfa_secret: str = db.Column(db.String(16), nullable=True)  # Assume TOTP uses secrets of fixed length 16

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def enable_mfa(self, secret: str):
        self.mfa_enabled = True
        self.mfa_secret = secret

    def disable_mfa(self):
        self.mfa_enabled = False
        self.mfa_secret = None

    def __repr__(self) -> str:
        return f"<User {self.username}>"