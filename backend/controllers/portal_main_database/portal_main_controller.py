# Epic Title: Core Banking System Integration

from flask import Blueprint, request, jsonify
from backend.services.portal_main_database.portal_main_service import PortalMainService

portal_main_controller = Blueprint('portal_main_controller', __name__)

@portal_main_controller.route('/portal_main', methods=['POST'])
def add_data():
    data = request.json.get('data')
    if not data:
        return jsonify({'message': 'Data is required'}), 400

    data_entry = PortalMainService.add_data(data)
    return jsonify({
        'id': data_entry.id,
        'data': data_entry.data,
        'created_at': data_entry.created_at
    })

@portal_main_controller.route('/portal_main', methods=['GET'])
def get_all_data():
    all_data = PortalMainService.get_all_data()
    data_list = [{
        'id': data.id,
        'data': data.data,
        'created_at': data.created_at
    } for data in all_data]
    return jsonify(data_list)

# File 5: Register Portal Main Controller Blueprint in app.py (Already Exists, Modified)