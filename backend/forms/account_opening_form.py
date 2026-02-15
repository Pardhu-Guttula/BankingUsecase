# Epic Title: Account Opening and Service Modifications

from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SelectField
from wtforms.validators import DataRequired, Email, NumberRange

class AccountOpeningForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    initial_deposit = DecimalField('Initial Deposit', validators=[DataRequired(), NumberRange(min=0.0)])
    account_type = SelectField('Account Type', choices=[('savings', 'Savings'), ('checking', 'Checking')], validators=[DataRequired()])

# File 3: Account Opening Controller for Handling Form Submission in account/controllers/account_opening_controller.py