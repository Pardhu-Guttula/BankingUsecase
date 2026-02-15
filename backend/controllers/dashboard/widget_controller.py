# Epic Title: Personalized Dashboard

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from backend.services.dashboard.widget_service import WidgetService

widget_controller = Blueprint('widget_controller', __name__)

@widget_controller.route('/dashboard/widgets', methods=['POST'])
@login_required
def add_widget():
    data = request.get_json()
    widget_type = data.get('widget_type')

    if not widget_type:
        return jsonify({'message': 'Widget type is required'}), 400

    widget = WidgetService.add_widget(current_user.id, widget_type)
    return jsonify({
        'id': widget.id,
        'user_id': widget.user_id,
        'widget_type': widget.widget_type
    }), 201

@widget_controller.route('/dashboard/widgets/<int:widget_id>', methods=['DELETE'])
@login_required
def remove_widget(widget_id: int):
    WidgetService.remove_widget(current_user.id, widget_id)
    return jsonify({'message': 'Widget removed successfully'}), 200

@widget_controller.route('/dashboard/widgets', methods=['GET'])
@login_required
def get_widgets():
    widgets = WidgetService.get_user_widgets(current_user.id)
    widgets_list = [{'id': w.id, 'widget_type': w.widget_type} for w in widgets]
    return jsonify(widgets_list)

# File 5: Register Widget Controller Blueprint in app.py (Already Exists, Modified)