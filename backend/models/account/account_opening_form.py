# Epic Title: Account Opening and Service Modifications

from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField
from wtforms.validators import DataRequired, Email, Length, NumberRange

class AccountOpeningForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(max=100)])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=18, max=100)])
    initial_deposit = IntegerField('Initial Deposit', validators=[DataRequired(), NumberRange(min=0)])


# File 2: Account Model for Opening Accounts in models/accounts/account_model.py