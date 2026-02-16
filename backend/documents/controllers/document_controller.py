# Epic Title: Interaction History and Documentation Upload

from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required
from backend.documents.services.document_service import DocumentService

document_blueprint = Blueprint('documents', __name__)
document_service = None  # Will be initialized in app.py

@document_blueprint.route('/upload', methods=['POST'])
@jwt_required()
def upload_document():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    request_id = request.form.get('request_id')
    if not request_id:
        return jsonify({"error": "No request ID provided"}), 400

    document = document_service.save_document(request_id, file)
    return jsonify({
        "id": document.id,
        "filename": document.filename,
        "filepath": document.filepath,
        "uploaded_at": document.uploaded_at
    }), 201

@document_blueprint.route('/documents/<int:request_id>', methods=['GET'])
@jwt_required()
def get_documents(request_id: int):
    documents = document_service.get_documents_for_request(request_id)
    return jsonify([{
        "id": doc.id,
        "filename": doc.filename,
        "filepath": doc.filepath,
        "uploaded_at": doc.uploaded_at
    } for doc in documents]), 200