# Epic Title: Role-based Access Control

from sqlalchemy import Column, Integer, ForeignKey
from backend.app import db

class RolePolicy(db.Model):
    __tablename__ = 'role_policies'

    role_id = Column(Integer, ForeignKey('roles.id'), primary_key=True)
    policy_id = Column(Integer, ForeignKey('policies.id'), primary_key=True)

    def __init__(self, role_id: int, policy_id: int):
        self.role_id = role_id
        self.policy_id = policy_id


# File 3: Policy Repository for CRUD Operations in access_control/roles/policy_repository.py