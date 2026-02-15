# Epic Title: Customizable Widgets

from flask import Blueprint, request, jsonify
from dashboard.services.widget_service import WidgetService
from flask_login import login_required, current_user

widget_controller = Blueprint('widget_controller', __name__)

@widget_controller.route('/widgets', methods=['GET'])
@login_required
def get_user_widgets():
    user_id = current_user.id
    widgets = WidgetService.get_user_widgets(user_id)
    return jsonify(widgets), 200

@widget_controller.route('/widgets', methods=['POST'])
@login_required
def add_widget():
    data = request.json
    user_id = current_user.id
    name = data.get('name')
    settings = data.get('settings', '')

    if not name:
        return jsonify({"error": "Widget name is required"}), 400

    widget = WidgetService.add_widget(user_id, name, settings)
    return jsonify({
        "id": widget.id,
        "name": widget.name,
        "settings": widget.settings
    }), 201

@widget_controller.route('/widgets/<int:widget_id>', methods=['DELETE'])
@login_required
def remove_widget(widget_id: int):
    success = WidgetService.remove_widget(widget_id)
    if success:
        return jsonify({"message": "Widget removed successfully"}), 200
    else:
        return jsonify({"error": "Widget not found"}), 404


# File 5: App Update to Register Widget Controller in app.py