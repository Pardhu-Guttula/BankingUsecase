# Epic Title: Display Tailored Products

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    profile = db.Column(db.String(150), nullable=False)  # Profile field added

    def set_password(self, password: str) -> None:
        # Epic Title: Display Tailored Products
        self.password = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        # Epic Title: Display Tailored Products
        return check_password_hash(self.password, password)