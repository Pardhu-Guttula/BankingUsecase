# Epic Title: Define User Roles

from backend.app import db

class UserRole(db.Model):
    __tablename__ = 'user_roles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)

    role = db.relationship('Role', backref='user_roles')

    def __init__(self, user_id: int, role_id: int):
        self.user_id = user_id
        self.role_id = role_id


# File 3: Role Repository for Database Operations in accesscontrol/repositories/role_repository.py