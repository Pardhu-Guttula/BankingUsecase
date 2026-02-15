# Epic Title: Assign Permissions to Roles

from sqlalchemy import Column, Integer, String
from backend.app import db

class Permission(db.Model):
    __tablename__ = 'permissions'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255))

    def __init__(self, name: str, description: str = None):
        self.name = name
        self.description = description


# File 2: Role-Permission Association Model in `models/access_control/role_permission_model.py`