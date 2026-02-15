# Epic Title: Service Modification Requests

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from ..services.service_modification_request_service import ServiceModificationRequestService

service_modification_request_controller = Blueprint('service_modification_request_controller', __name__)
service_modification_request_service = ServiceModificationRequestService()

@service_modification_request_controller.route('/service_modification_requests', methods=['POST'])
@login_required
def create_service_modification_request():
    service_name = request.json.get('service_name')

    if not service_name:
        return jsonify({"error": "Service name is required"}), 400

    success = service_modification_request_service.create_service_modification_request(current_user.id, service_name)
    if success:
        return jsonify({"message": "Service modification request submitted successfully"}), 200
    return jsonify({"error": "Failed to submit service modification request"}), 500

@service_modification_request_controller.route('/service_modification_requests', methods=['GET'])
@login_required
def get_service_modification_requests():
    service_modification_requests = service_modification_request_service.get_service_modification_requests(current_user.id)
    return jsonify(service_modification_requests), 200



# File 4: ServiceModificationRequest Service in account/services/service_modification_request_service.py