# Epic Title: Secure User Data

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    mobile = db.Column(db.String(300), nullable=False)  # Encrypted mobile number

    def save(self):
        # Epic Title: Secure User Data
        db.session.add(self)
        db.session.commit()