# Epic Title: Account Opening and Service Modifications

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from backend.forms.account_opening_form import AccountOpeningForm
from backend.account.services.account_service import AccountService

account_opening_controller = Blueprint('account_opening_controller', __name__)

@account_opening_controller.route('/open_account', methods=['GET', 'POST'])
@login_required
def open_account():
    form = AccountOpeningForm()
    if form.validate_on_submit():
        user_id = current_user.id
        full_name = form.full_name.data
        email = form.email.data
        initial_deposit = form.initial_deposit.data
        account_type = form.account_type.data
        if AccountService.open_account(user_id, full_name, email, initial_deposit, account_type):
            flash('Account opening request submitted successfully.', 'success')
        else:
            flash('Failed to submit account opening request.', 'danger')
        return redirect(url_for('dashboard_controller.dashboard'))
    return render_template('account_opening.html', form=form)

# File 4: Account Model Update for New Account Creation in models/accounts/account_model.py