# Epic Title: Maintain Separate Database

from flask import Blueprint, request, jsonify
from flask_login import login_required
from backend.services.portal_main_database.portal_main_service import PortalMainService

portal_main_controller = Blueprint('portal_main_controller', __name__)

@portal_main_controller.route('/portal/data', methods=['POST'])
@login_required
def save_data():
    data = request.get_json()
    data_key = data.get('data_key')
    data_value = data.get('data_value')

    if not data_key or not data_value:
        return jsonify({'message': 'Data key and value are required'}), 400

    try:
        PortalMainService.save_data(data_key, data_value)
        return jsonify({'message': 'Data saved successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@portal_main_controller.route('/portal/data/<string:data_key>', methods=['GET'])
@login_required
def get_data(data_key: str):
    try:
        data = PortalMainService.get_data_by_key(data_key)
        if data:
            return jsonify({'data_key': data.data_key, 'data_value': data.data_value, 'created_at': data.created_at.isoformat()}), 200
        else:
            return jsonify({'message': 'Data not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@portal_main_controller.route('/portal/data', methods=['GET'])
@login_required
def get_all_data():
    try:
        data_list = PortalMainService.get_all_data()
        return jsonify([{'data_key': data.data_key, 'data_value': data.data_value, 'created_at': data.created_at.isoformat()} for data in data_list]), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500


# File 5: Schema for Portal Main Data Table in `database/create_portal_main_data_table.sql`