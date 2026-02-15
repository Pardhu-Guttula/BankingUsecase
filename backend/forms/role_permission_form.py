# Epic Title: Role-based Access Control

from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.validators import DataRequired
from backend.services.access_control.role_service import RoleService

class RolePermissionForm(FlaskForm):
    roles = SelectField('Select Role', validators=[DataRequired()])
    permissions = SelectField('Select Permission', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        super(RolePermissionForm, self).__init__(*args, **kwargs)
        self.roles.choices = [(role.id, role.name) for role in RoleService.get_all_roles()]
        self.permissions.choices = [(permission.id, permission.name) for permission in RoleService.get_all_permissions()]


# File 9: Permission Controller to Manage Permissions in controllers/dashboard/permission_controller.py