# Epic Title: Interaction History and Documentation Upload

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from backend.forms.application_form.py import ApplicationForm
from backend.services.interactions.application_service.py import ApplicationService

application_controller = Blueprint('application_controller', __name__)

@application_controller.route('/applications', methods=['GET'])
@login_required
def view_applications():
    user_id = current_user.id
    applications = ApplicationService.get_user_applications(user_id)
    return render_template('applications.html', applications=applications)

@application_controller.route('/applications/new', methods=['GET', 'POST'])
@login_required
def new_application():
    form = ApplicationForm()
    if form.validate_on_submit():
        user_id = current_user.id
        data = form.data.data
        ApplicationService.save_application(user_id, 'incomplete', data)
        return redirect(url_for('application_controller.view_applications'))
    return render_template('new_application.html', form=form)

@application_controller.route('/applications/edit/<int:application_id>', methods=['GET', 'POST'])
@login_required
def edit_application(application_id: int):
    application = ApplicationService.get_application_by_id(application_id)
    if not application or application.user_id != current_user.id:
        return redirect(url_for('application_controller.view_applications'))

    form = ApplicationForm()
    if form.validate_on_submit():
        application.data = form.data.data
        ApplicationService.save_application(application.user_id, application.status, application.data)
        return redirect(url_for('application_controller.view_applications'))

    form.data.data = application.data
    form.application_id.data = application.id
    return render_template('edit_application.html', form=form, application=application)


# File 7: Templates to Manage and Edit Applications
## Applications Template in templates/applications.html