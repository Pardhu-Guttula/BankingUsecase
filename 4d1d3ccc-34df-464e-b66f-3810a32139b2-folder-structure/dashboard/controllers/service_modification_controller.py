# Epic Title: Service Modification Requests

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from dashboard.services.service_modification_service import ServiceModificationService

service_modification_controller = Blueprint('service_modification_controller', __name__)

@service_modification_controller.route('/service-modification-requests', methods=['POST'])
@login_required
def request_service_modification():
    data = request.json
    account_id = data.get('account_id')
    service = data.get('service')
    user_id = current_user.id

    if not account_id or not service:
        return jsonify({"error": "Account ID and service are required"}), 400

    request = ServiceModificationService.request_service_modification(user_id, account_id, service)
    return jsonify({
        "id": request.id,
        "account_id": request.account_id,
        "service": request.service,
        "status": request.status,
        "created_at": request.created_at
    }), 201

@service_modification_controller.route('/service-modification-requests', methods=['GET'])
@login_required
def get_user_requests():
    user_id = current_user.id
    requests = ServiceModificationService.get_user_requests(user_id)
    return jsonify(requests), 200


# File 5: App Update to Register Service Modification Controller in app.py