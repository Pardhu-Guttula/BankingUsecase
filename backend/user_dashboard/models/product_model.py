# Epic Title: Display Tailored Products

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    profile = db.Column(db.String(150), nullable=False)
    eligibility = db.Column(db.String(150), nullable=True)