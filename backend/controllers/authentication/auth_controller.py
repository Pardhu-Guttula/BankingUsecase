# Epic Title: User Authentication and Security

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, logout_user
from backend.forms.mfa_form import MFAForm
from backend.auth.services.authentication_service import AuthenticationService

auth_controller = Blueprint('auth_controller', __name__)

@auth_controller.route('/login', methods=['GET', 'POST'])
def login():
    form = MFAForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        token = form.token.data
        if AuthenticationService.login_with_mfa(username, password, token):
            return redirect(url_for('dashboard_controller.dashboard'))
        else:
            flash('Invalid username, password or MFA token', 'danger')
    return render_template('login.html', form=form)

@auth_controller.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_controller.login'))


# File 6: Login Template for MFA in templates/login.html