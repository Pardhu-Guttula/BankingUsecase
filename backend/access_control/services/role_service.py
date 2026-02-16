# Epic Title: Role-based Access Control

from backend.access_control.models.role import Role, UserRole, db

class RoleService:
    def __init__(self):
        pass

    def create_role(self, name: str, description: str) -> Role:
        role = Role(name=name, description=description)
        db.session.add(role)
        db.session.commit()
        return role

    def assign_role_to_user(self, user_id: int, role_id: int) -> UserRole:
        user_role = UserRole(user_id=user_id, role_id=role_id)
        db.session.add(user_role)
        db.session.commit()
        return user_role

    def get_roles(self) -> list[Role]:
        return Role.query.all()

    def get_user_roles(self, user_id: int) -> list[UserRole]:
        return UserRole.query.filter_by(user_id=user_id).all()