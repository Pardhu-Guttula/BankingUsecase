# Epic Title: Account Opening and Service Modifications

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.models.account.service_modification_form import ServiceModificationForm
from backend.services.account.modifications.service_modification_service import ServiceModificationService

service_modification_controller = Blueprint('service_modification_controller', __name__)

@service_modification_controller.route('/modify_service', methods=['POST'])
@login_required
def modify_service():
    form = ServiceModificationForm(request.form)
    if form.validate_on_submit():
        service_modification = ServiceModificationService.modify_service(
            user_id=current_user.id,
            service_name=form.service_name.data,
            action=form.action.data
        )
        return jsonify({"message": "Service modification request submitted successfully", "modification_id": service_modification.id}), 201
    else:
        return jsonify({"errors": form.errors}), 400


# File 7: Update Main App to Register Service Modification Controller in app.py