# Epic Title: Role-based Access Control

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class PermissionForm(FlaskForm):
    name = StringField('Permission Name', validators=[DataRequired()])
    description = TextAreaField('Description')


# File 8: Role Permission Form to Assign Permissions to Roles in forms/role_permission_form.py