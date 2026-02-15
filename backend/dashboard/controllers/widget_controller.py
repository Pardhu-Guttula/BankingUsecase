# Epic Title: Personalized Dashboard

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.dashboard.widget_service import WidgetService

widget_controller = Blueprint('widget_controller', __name__)

@widget_controller.route('/widgets', methods=['GET'])
@login_required
def get_user_widgets():
    widgets = WidgetService.get_user_widgets(current_user.id)
    return jsonify([{
        'id': widget.id,
        'widget_type': widget.widget_type,
        'data_source': widget.data_source,
        'position': widget.position,
        'is_active': widget.is_active
    } for widget in widgets])

@widget_controller.route('/widgets', methods=['POST'])
@login_required
def create_widget():
    data = request.get_json()
    widget = WidgetService.create_widget(
        user_id=current_user.id,
        widget_type=data['widget_type'],
        data_source=data['data_source'],
        position=data['position']
    )
    return jsonify({'id': widget.id, 'message': 'Widget created successfully'}), 201

@widget_controller.route('/widgets/<int:widget_id>', methods=['PUT'])
@login_required
def update_widget(widget_id):
    data = request.get_json()
    widget = WidgetService.update_widget(
        widget_id=widget_id,
        widget_type=data.get('widget_type'),
        data_source=data.get('data_source'),
        position=data.get('position'),
        is_active=data.get('is_active')
    )
    return jsonify({'id': widget.id, 'message': 'Widget updated successfully'}), 200

@widget_controller.route('/widgets/<int:widget_id>', methods=['DELETE'])
@login_required
def delete_widget(widget_id):
    WidgetService.delete_widget(widget_id)
    return jsonify({'message': 'Widget deleted successfully'}), 200


# File 5: Dashboard Controller for Context in dashboard/controllers/dashboard_controller.py (Already Exists, Re-emitting for Context)