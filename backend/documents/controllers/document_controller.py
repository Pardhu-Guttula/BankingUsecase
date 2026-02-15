# Epic Title: Interaction History and Documentation Upload

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.documents.services.document_service import DocumentService

document_controller = Blueprint('document_controller', __name__)

@document_controller.route('/upload', methods=['POST'])
@login_required
def upload_document():
    if 'file' not in request.files:
        return jsonify({"message": "No file part."}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "No selected file."}), 400
    if DocumentService.save_document(file, current_user.id):
        return jsonify({"message": "Document uploaded successfully."}), 201
    return jsonify({"message": "Failed to upload document."}), 500


# File 5: Update Main App to Register Document Controller and Configure Upload Folder in app.py