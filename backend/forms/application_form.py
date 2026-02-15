# Epic Title: Interaction History and Documentation Upload

from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField
from wtforms.validators import DataRequired

class ApplicationForm(FlaskForm):
    data = TextAreaField('Application Data', validators=[DataRequired()])
    application_id = HiddenField('Application ID')


# File 6: Application Controller to Manage Applications in controllers/dashboard/application_controller.py