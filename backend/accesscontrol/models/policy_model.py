# Epic Title: Access Policies for Different Roles

from backend.app import db

class Policy(db.Model):
    __tablename__ = 'policies'

    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    resource = db.Column(db.String(100), nullable=False)
    can_view = db.Column(db.Boolean, default=False, nullable=False)
    can_edit = db.Column(db.Boolean, default=False, nullable=False)
    can_delete = db.Column(db.Boolean, default=False, nullable=False)

    role = db.relationship('Role', backref='policies')

    def __init__(self, role_id: int, resource: str, can_view: bool, can_edit: bool, can_delete: bool):
        self.role_id = role_id
        self.resource = resource
        self.can_view = can_view
        self.can_edit = can_edit
        self.can_delete = can_delete


# File 2: Policy Repository for Database Operations in accesscontrol/repositories/policy_repository.py