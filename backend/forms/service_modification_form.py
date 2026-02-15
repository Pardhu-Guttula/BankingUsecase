# Epic Title: Account Opening and Service Modifications

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class ServiceModificationForm(FlaskForm):
    service_name = StringField('Service Name', validators=[DataRequired()])
    modification_type = SelectField('Modification Type', choices=[('add', 'Add'), ('remove', 'Remove')], validators=[DataRequired()])
    reason = TextAreaField('Reason for Modification', validators=[DataRequired()])


# File 2: Service Modification Controller to Handle Requests in account/controllers/service_modification_controller.py