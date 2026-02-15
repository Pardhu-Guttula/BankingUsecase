# Epic Title: Assign Permissions to Roles

from backend.app import db

class RolePermission(db.Model):
    __tablename__ = 'role_permissions'

    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    permission_id = db.Column(db.Integer, db.ForeignKey('permissions.id'), nullable=False)

    role = db.relationship('Role', backref='role_permissions')
    permission = db.relationship('Permission', backref='role_permissions')

    def __init__(self, role_id: int, permission_id: int):
        self.role_id = role_id
        self.permission_id = permission_id


# File 3: Permission Repository for Database Operations in accesscontrol/repositories/permission_repository.py