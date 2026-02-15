# Epic Title: Interaction History and Documentation Upload

from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import login_required, current_user
from backend.forms.document_upload_form import DocumentUploadForm
from backend.services.interactions.document_service import DocumentService

document_controller = Blueprint('document_controller', __name__)

@document_controller.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_document():
    form = DocumentUploadForm()
    if form.validate_on_submit():
        user_id = current_user.id
        request_id = form.request_id.data
        document = form.document.data
        DocumentService.upload_document(user_id, request_id, document)
        return redirect(url_for('document_controller.upload_document'))
    return render_template('upload.html', form=form)


# File 7: Upload Page Template for Document Upload in templates/upload.html