# Epic Title: Assign Permissions to Roles

from sqlalchemy import Column, Integer, ForeignKey
from backend.app import db

class RolePermission(db.Model):
    __tablename__ = 'role_permissions'

    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)
    permission_id = Column(Integer, ForeignKey('permissions.id'), nullable=False)

    def __init__(self, role_id: int, permission_id: int):
        self.role_id = role_id
        self.permission_id = permission_id


# File 3: Permission Repository in `repositories/access_control/permission_repository.py`