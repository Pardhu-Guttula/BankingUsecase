# Epic Title: Account Opening and Service Modifications

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.models.account.account_opening_form import AccountOpeningForm
from backend.services.account.opening.account_opening_service import AccountOpeningService

account_opening_controller = Blueprint('account_opening_controller', __name__)

@account_opening_controller.route('/open_account', methods=['POST'])
@login_required
def open_account():
    form = AccountOpeningForm(request.form)
    if form.validate_on_submit():
        account = AccountOpeningService.open_account(
            user_id=current_user.id,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            age=form.age.data,
            initial_deposit=form.initial_deposit.data
        )
        return jsonify({"message": "Account opened successfully", "account_id": account.id}), 201
    else:
        return jsonify({"errors": form.errors}), 400


# File 6: Update Main App to Register Account Opening Controller in app.py