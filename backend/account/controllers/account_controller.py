# Epic Title: Account Opening and Service Modifications

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from backend.forms.account_opening_form import AccountOpeningForm
from backend.account.services.account_service import AccountService

account_controller = Blueprint('account_controller', __name__)

@account_controller.route('/open_account', methods=['GET', 'POST'])
@login_required
def open_account():
    form = AccountOpeningForm()
    if form.validate_on_submit():
        full_name = form.full_name.data
        email = form.email.data
        initial_deposit = form.initial_deposit.data
        account_type = form.account_type.data
        result = AccountService.open_account(current_user.id, full_name, email, initial_deposit, account_type)
        if result:
            flash('Account opening request submitted successfully.', 'success')
            return redirect(url_for('dashboard_controller.dashboard'))
        else:
            flash('An error occurred while processing your request.', 'danger')
    return render_template('open_account.html', form=form)


# File 3: Account Service to Handle Business Logic for Opening Accounts in account/services/account_service.py