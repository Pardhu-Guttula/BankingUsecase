# Epic Title: Interaction History and Documentation Upload

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.documents.services import DocumentService

document_upload_blueprint = Blueprint('document_upload', __name__)
# Initialize DocumentService later in app.py to inject dependencies
document_service = None  # Placeholder for real instance

@document_upload_blueprint.route('/upload/<int:request_id>', methods=['POST'])
@jwt_required()
def upload_document(request_id: int):
    current_user_id = get_jwt_identity()
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    try:
        document = document_service.save_document(current_user_id, request_id, file)
        return jsonify({"message": "File uploaded successfully", "document_id": document.id}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400