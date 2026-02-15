# Epic Title: Customizable Widgets

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from ..services.widget_service import WidgetService

widget_controller = Blueprint('widget_controller', __name__)
widget_service = WidgetService()

@widget_controller.route('/widgets', methods=['POST'])
@login_required
def add_widget():
    widget_type = request.json.get('widget_type')
    settings = request.json.get('settings')
    
    if widget_service.add_widget(current_user.id, widget_type, settings):
        return jsonify({"message": "Widget added successfully"}), 200
    return jsonify({"message": "Failed to add widget"}), 400

@widget_controller.route('/widgets/<int:widget_id>', methods=['DELETE'])
@login_required
def remove_widget(widget_id):
    if widget_service.remove_widget(current_user.id, widget_id):
        return jsonify({"message": "Widget removed successfully"}), 200
    return jsonify({"message": "Failed to remove widget"}), 400

@widget_controller.route('/widgets', methods=['GET'])
@login_required
def get_widgets():
    widgets = widget_service.get_widgets(current_user.id)
    return jsonify(widgets), 200



# File 4: Widget Service Implementation in dashboard/services/widget_service.py