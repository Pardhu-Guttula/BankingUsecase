# Epic Title: Account Opening and Service Modifications

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import DataRequired, Email, NumberRange

class AccountOpeningForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    initial_deposit = FloatField('Initial Deposit', validators=[DataRequired(), NumberRange(min=0)])
    account_type = SelectField('Account Type', choices=[('savings', 'Savings'), ('checking', 'Checking')], validators=[DataRequired()])


# File 2: Account Controller for Account Opening in account/controllers/account_controller.py