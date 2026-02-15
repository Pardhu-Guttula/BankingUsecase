# Epic Title: Personalized Dashboard

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from backend.services.dashboard.widget_service import WidgetService

widget_controller = Blueprint('widget_controller', __name__)

@widget_controller.route('/widgets', methods=['POST'])
@login_required
def add_widget():
    data = request.get_json()
    name = data.get('name')
    position = data.get('position')

    if not name or position is None:
        return jsonify({'message': 'Name and position are required'}), 400

    widget = WidgetService.add_widget(current_user.id, name, position)
    return jsonify({
        'id': widget.id,
        'name': widget.name,
        'position': widget.position
    }), 201

@widget_controller.route('/widgets/<int:widget_id>', methods=['DELETE'])
@login_required
def remove_widget(widget_id: int):
    WidgetService.remove_widget(widget_id)
    return jsonify({'message': 'Widget removed successfully'}), 200

@widget_controller.route('/widgets', methods=['GET'])
@login_required
def get_widgets():
    user_widgets = WidgetService.get_user_widgets(current_user.id)
    widgets_list = [{'id': widget.id, 'name': widget.name, 'position': widget.position} for widget in user_widgets]
    return jsonify(widgets_list)

# File 5: Register Widget Controller Blueprint in app.py (Already Exists, Modified)