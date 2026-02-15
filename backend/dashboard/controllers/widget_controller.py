# Epic Title: Personalized Dashboard

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.dashboard.widget_service import WidgetService

widget_controller = Blueprint('widget_controller', __name__)

@widget_controller.route('/widgets', methods=['POST'])
@login_required
def add_widget():
    data = request.get_json()
    widget_type = data.get('widget_type')
    position = data.get('position')
    if not widget_type or position is None:
        return jsonify({'message': 'Widget type and position are required'}), 400

    widget = WidgetService.add_widget(current_user.id, widget_type, position)
    return jsonify({
        'id': widget.id,
        'widget_type': widget.widget_type,
        'position': widget.position
    }), 201

@widget_controller.route('/widgets/<int:widget_id>', methods=['DELETE'])
@login_required
def remove_widget(widget_id: int):
    WidgetService.remove_widget(current_user.id, widget_id)
    return jsonify({'message': 'Widget removed successfully'}), 200

@widget_controller.route('/widgets', methods=['GET'])
@login_required
def get_user_widgets():
    widgets = WidgetService.get_user_widgets(current_user.id)
    widget_list = [{
        'id': widget.id,
        'widget_type': widget.widget_type,
        'position': widget.position
    } for widget in widgets]
    return jsonify(widget_list), 200


# File 5: Register Widget Controller Blueprint in app.py (Already Exists, Modified)