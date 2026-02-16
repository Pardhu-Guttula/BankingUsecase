# Epic Title: Role-based Access Control

import logging
from flask_sqlalchemy import SQLAlchemy
from backend.access_control.models import Role, UserRole

logger = logging.getLogger(__name__)

class RoleService:
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def create_role(self, name: str, description: str = "") -> Role:
        if Role.query.filter_by(name=name).first():
            raise ValueError(f"Role with name '{name}' already exists.")
        role = Role(name=name, description=description)
        self.db.session.add(role)
        self.db.session.commit()
        logger.info(f"Created role: {role}")
        return role

    def assign_role_to_user(self, user_id: int, role_id: int) -> UserRole:
        if UserRole.query.filter_by(user_id=user_id, role_id=role_id).first():
            raise ValueError(f"User {user_id} already has role {role_id}.")
        user_role = UserRole(user_id=user_id, role_id=role_id)
        self.db.session.add(user_role)
        self.db.session.commit()
        logger.info(f"Assigned role {role_id} to user {user_id}")
        return user_role

    def get_roles(self) -> list[Role]:
        return Role.query.all()

    def get_user_roles(self, user_id: int) -> list[UserRole]:
        return UserRole.query.filter_by(user_id=user_id).all()