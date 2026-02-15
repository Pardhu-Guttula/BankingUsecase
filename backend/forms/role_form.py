# Epic Title: Role-based Access Control

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class RoleForm(FlaskForm):
    name = StringField('Role Name', validators=[DataRequired()])
    description = TextAreaField('Description')


# File 7: Role Controller to Manage Roles in controllers/dashboard/role_controller.py