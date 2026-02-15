# Epic Title: Document Upload Capability

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
    try:
        document = DocumentService.upload_document(current_user.id, file)
        return jsonify({'message': 'File uploaded successfully', 'document': document.serialize()}), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400


# File 5: Schema for Documents Table in `database/create_documents_table.sql`