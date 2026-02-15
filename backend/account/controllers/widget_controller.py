# Epic Title: Personalized Dashboard

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.account.services.widget_service import WidgetService

widget_controller = Blueprint('widget_controller', __name__)

@widget_controller.route('/widgets', methods=['POST'])
@login_required
def add_widget():
    data = request.get_json()
    name = data.get('name')
    settings = data.get('settings', '')
    if WidgetService.add_widget(current_user.id, name, settings):
        return jsonify({"message": "Widget added successfully."}), 201
    return jsonify({"message": "Failed to add widget."}), 500

@widget_controller.route('/widgets/<int:widget_id>', methods=['DELETE'])
@login_required
def remove_widget(widget_id):
    if WidgetService.remove_widget(widget_id):
        return jsonify({"message": "Widget removed successfully."}), 200
    return jsonify({"message": "Failed to remove widget."}), 500


# File 5: Update Dashboard HTML Template to Support Adding and Removing Widgets in templates/dashboard.html