# Epic Title: Interaction History and Documentation Upload

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from dashboard.services.document_service import DocumentService

document_upload_controller = Blueprint('document_upload_controller', __name__)

@document_upload_controller.route('/documents/upload', methods=['POST'])
@login_required
def upload_document():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    request_id = request.form.get('request_id')

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    document = DocumentService.upload_document(current_user.id, int(request_id), file)
    return jsonify({
        "id": document.id,
        "filename": document.filename,
        "uploaded_at": document.uploaded_at
    }), 201

@document_upload_controller.route('/documents/<int:request_id>', methods=['GET'])
@login_required
def get_documents(request_id: int):
    documents = DocumentService.get_request_documents(request_id)
    return jsonify(documents), 200


# File 5: App Update to Register Document Upload Controller in app.py