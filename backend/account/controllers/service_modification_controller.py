# Epic Title: Account Opening and Service Modifications

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from backend.forms.service_modification_form import ServiceModificationForm
from backend.account.services.service_modification_service import ServiceModificationService

service_modification_controller = Blueprint('service_modification_controller', __name__)

@service_modification_controller.route('/modify_services', methods=['GET', 'POST'])
@login_required
def modify_services():
    form = ServiceModificationForm()
    if form.validate_on_submit():
        user_id = current_user.id
        service_type = form.service_type.data
        description = form.description.data
        if ServiceModificationService.modify_service(user_id, service_type, description):
            flash('Service modification request submitted successfully.', 'success')
        else:
            flash('Failed to submit service modification request.', 'danger')
        return redirect(url_for('dashboard_controller.dashboard'))
    return render_template('service_modification.html', form=form)

# File 4: Service Modification Model to Track Modification Requests in models/accounts/service_modification_model.py