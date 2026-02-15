# Epic Title: Maintain Separate Database

from core_integration.models import portal_db as db

# Define Portal DB models here

class PortalUser(db.Model):
    __tablename__ = 'portal_users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password


# File 5: Core Banking Database SQLAlchemy Bindings in core_integration/models/core_banking_db.py