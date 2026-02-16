# Epic Title: Role-based Access Control

from backend.access_control.models.permission import Permission, RolePermission, db

class PermissionService:
    def __init__(self):
        pass

    def create_permission(self, name: str, description: str) -> Permission:
        permission = Permission(name=name, description=description)
        db.session.add(permission)
        db.session.commit()
        return permission

    def assign_permission_to_role(self, role_id: int, permission_id: int) -> RolePermission:
        role_permission = RolePermission(role_id=role_id, permission_id=permission_id)
        db.session.add(role_permission)
        db.session.commit()
        return role_permission

    def get_permissions(self) -> list[Permission]:
        return Permission.query.all()

    def get_role_permissions(self, role_id: int) -> list[RolePermission]:
        return RolePermission.query.filter_by(role_id=role_id).all()