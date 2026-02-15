# Epic Title: Account Opening and Service Modifications

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from backend.forms.service_modification_form import ServiceModificationForm
from backend.account.services.service_modification_service import ServiceModificationService

service_modification_controller = Blueprint('service_modification_controller', __name__)

@service_modification_controller.route('/modify_service', methods=['GET', 'POST'])
@login_required
def modify_service():
    form = ServiceModificationForm()
    if form.validate_on_submit():
        service_name = form.service_name.data
        modification_type = form.modification_type.data
        reason = form.reason.data
        result = ServiceModificationService.modify_service(current_user.id, service_name, modification_type, reason)
        if result:
            flash('Service modification request submitted successfully.', 'success')
            return redirect(url_for('dashboard_controller.dashboard'))
        else:
            flash('An error occurred while processing your request.', 'danger')
    return render_template('modify_service.html', form=form)


# File 3: Service Modification Service to Handle Business Logic in account/services/service_modification_service.py