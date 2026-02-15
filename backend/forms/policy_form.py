# Epic Title: Role-based Access Control

from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.validators import DataRequired
from backend.services.access_control.role_service import RoleService

class PolicyForm(FlaskForm):
    role_id = SelectField('Select Role', validators=[DataRequired()])
    service_name = StringField('Service Name', validators=[DataRequired()])
    access_level = StringField('Access Level', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        super(PolicyForm, self).__init__(*args, **kwargs)
        self.role_id.choices = [(role.id, role.name) for role in RoleService.get_all_roles()]


# File 6: Policy Controller to Manage Policies in controllers/dashboard/policy_controller.py