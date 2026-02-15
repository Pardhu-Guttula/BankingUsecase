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
    widget_data = data.get('widget_data', '')

    if not widget_type:
        return jsonify({"message": "Widget type is required"}), 400

    widget = WidgetService.add_widget(current_user.id, widget_type, widget_data)
    return jsonify({"message": "Widget added successfully", "widget_id": widget.id}), 201

@widget_controller.route('/widgets/<int:widget_id>', methods=['DELETE'])
@login_required
def remove_widget(widget_id: int):
    WidgetService.remove_widget(widget_id)
    return jsonify({"message": "Widget removed successfully"}), 200

@widget_controller.route('/widgets', methods=['GET'])
@login_required
def get_widgets():
    widgets = WidgetService.get_widgets(current_user.id)
    return jsonify([{
        "id": widget.id,
        "widget_type": widget.widget_type,
        "widget_data": widget.widget_data
    } for widget in widgets]), 200


# File 6: Update Dashboard Controller to Integrate Widget Functionality in controllers/dashboard/dashboard_controller.py