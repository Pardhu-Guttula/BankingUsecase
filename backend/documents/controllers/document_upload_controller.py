# Epic Title: Interaction History and Documentation Upload

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.documents.document_upload_service import DocumentUploadService

document_upload_controller = Blueprint('document_upload_controller', __name__)

@document_upload_controller.route('/documents/upload', methods=['POST'])
@login_required
def upload_document():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    request_id = request.form.get('request_id')
    if not request_id:
        return jsonify({'message': 'Request ID not provided'}), 400

    document = DocumentUploadService.save_document(current_user.id, int(request_id), file)
    return jsonify({
        'file_name': document.file_name,
        'file_path': document.file_path
    }), 201


# File 5: Update Main App to Register Document Upload Controller Blueprint in app.py (Already Exists, Modified)