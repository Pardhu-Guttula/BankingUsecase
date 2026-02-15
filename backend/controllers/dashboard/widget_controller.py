# Epic Title: Personalized Dashboard

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.dashboard.widget_service import WidgetService

widget_controller = Blueprint('widget_controller', __name__)

@widget_controller.route('/widgets', methods=['GET'])
@login_required
def get_widgets():
    user_widgets = WidgetService.get_user_widgets(current_user.id)
    return jsonify([widget.__dict__ for widget in user_widgets]), 200

@widget_controller.route('/widgets', methods=['POST'])
@login_required
def add_widget():
    widget_type = request.json.get('widget_type')
    new_widget = WidgetService.add_widget_to_user(current_user.id, widget_type)
    return jsonify(new_widget.__dict__), 201

@widget_controller.route('/widgets/<int:widget_id>', methods=['DELETE'])
@login_required
def remove_widget(widget_id: int):
    success = WidgetService.remove_widget_from_user(current_user.id, widget_id)
    if success:
        return jsonify({"message": "Widget removed successfully"}), 200
    return jsonify({"error": "Widget not found"}), 404


# File 5: Update User Model to Include Relationship with Widget in models/authentication/user_model.py