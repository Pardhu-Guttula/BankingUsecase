# Epic Title: Define User Roles

from backend.app import db

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, name: str):
        self.name = name


# File 2: UserRole Association Model in accesscontrol/models/user_role_model.py