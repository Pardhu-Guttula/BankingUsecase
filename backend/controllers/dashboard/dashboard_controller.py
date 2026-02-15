# Epic Title: Customizable Widgets

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from backend.services.dashboard.widget_service import WidgetService

dashboard_controller = Blueprint('dashboard_controller', __name__)

@dashboard_controller.route('/dashboard/widgets', methods=['GET'])
@login_required
def get_widgets():
    widgets = WidgetService.get_widgets(current_user.id)
    return jsonify({'widgets': widgets}), 200

@dashboard_controller.route('/dashboard/widgets', methods=['POST'])
@login_required
def add_widget():
    data = request.get_json()
    widget_type = data.get('widget_type')
    position = data.get('position')

    WidgetService.add_widget(current_user.id, widget_type, position)
    return jsonify({'message': 'Widget added successfully'}), 201

@dashboard_controller.route('/dashboard/widgets/<int:widget_id>', methods=['DELETE'])
@login_required
def remove_widget(widget_id: int):
    WidgetService.remove_widget(widget_id)
    return jsonify({'message': 'Widget removed successfully'}), 200


# File 5: Update app.py for Widget Functionality