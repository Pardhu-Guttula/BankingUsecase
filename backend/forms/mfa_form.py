# Epic Title: User Authentication and Security

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class MFAForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    token = StringField('MFA Token', validators=[DataRequired()])


# File 5: Authentication Controller for MFA Login in controllers/authentication/auth_controller.py