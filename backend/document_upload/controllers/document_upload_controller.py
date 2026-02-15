# Epic Title: Interaction History and Documentation Upload

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.documents.document_service import DocumentService

document_upload_controller = Blueprint('document_upload_controller', __name__)

@document_upload_controller.route('/documents/upload', methods=['POST'])
@login_required
def upload_document():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No file selected for uploading'}), 400

    request_id = request.form.get('request_id')
    if not request_id:
        return jsonify({'message': 'Request ID is required'}), 400

    user_id = current_user.id
    document = DocumentService.save_document(user_id, int(request_id), file)
    return jsonify({
        'id': document.id,
        'filename': document.filename,
        'filepath': document.filepath,
        'uploaded_at': document.uploaded_at
    }), 201

@document_upload_controller.route('/documents', methods=['GET'])
@login_required
def get_user_documents():
    user_id = current_user.id
    documents = DocumentService.get_user_documents(user_id)
    documents_list = [{
        'id': document.id,
        'filename': document.filename,
        'filepath': document.filepath,
        'uploaded_at': document.uploaded_at
    } for document in documents]
    return jsonify(documents_list)

# File 5: Register Document Upload Controller Blueprint in app.py (Already Exists, Modified)