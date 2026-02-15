# Epic Title: Document Upload Capability

from flask import Blueprint, request, jsonify, current_app
from flask_login import login_required, current_user
from backend.interaction_history.services.document_service import DocumentService

document_controller = Blueprint('document_controller', __name__)

@document_controller.route('/upload', methods=['POST'])
@login_required
def upload_document():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        filename = DocumentService.save_document(file, current_user.id)
        return jsonify({"message": f"File {filename} uploaded successfully"}), 200


# File 5: Document Upload Template in user_dashboard/templates/upload.html