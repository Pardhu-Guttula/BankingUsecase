# Epic Title: Interaction History and Documentation Upload

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.documents.document_service import DocumentService

document_upload_controller = Blueprint('document_upload_controller', __name__)

@document_upload_controller.route('/documents/upload', methods=['POST'])
@login_required
def upload_document():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    document = DocumentService.save_document(file, current_user.id)
    return jsonify({
        'id': document.id,
        'user_id': document.user_id,
        'filename': document.filename,
        'file_path': document.file_path,
        'uploaded_at': document.uploaded_at
    })

# File 5: Register Document Upload Controller Blueprint in app.py (Already Exists, Modified)