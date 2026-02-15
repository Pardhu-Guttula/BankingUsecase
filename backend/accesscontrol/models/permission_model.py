# Epic Title: Assign Permissions to Roles

from backend.app import db

class Permission(db.Model):
    __tablename__ = 'permissions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, name: str):
        self.name = name


# File 2: RolePermission Association Model in accesscontrol/models/role_permission_model.py