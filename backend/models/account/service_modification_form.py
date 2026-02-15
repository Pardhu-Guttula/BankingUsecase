# Epic Title: Account Opening and Service Modifications

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

class ServiceModificationForm(FlaskForm):
    user_id = IntegerField('User ID', validators=[DataRequired()])
    service_name = StringField('Service Name', validators=[DataRequired(), Length(min=2, max=100)])
    action = StringField('Action', validators=[DataRequired(), Length(min=2, max=50)])

    
# File 2: Service Modification Model in models/account/service_modification_model.py