# Epic Title: Customizable Widgets

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.dashboard.services.widget_service import WidgetService

widget_blueprint = Blueprint('widgets', __name__)
widget_service = WidgetService(db)

@widget_blueprint.route('/widgets', methods=['GET'])
@jwt_required()
def get_widgets():
    current_user_id = get_jwt_identity()
    widgets = widget_service.get_widgets_by_user_id(current_user_id)
    return jsonify([{
        "id": widget.id,
        "widget_type": widget.widget_type,
        "settings": widget.settings,
        "created_at": widget.created_at
    } for widget in widgets]), 200

@widget_blueprint.route('/widgets', methods=['POST'])
@jwt_required()
def add_widget():
    current_user_id = get_jwt_identity()
    data = request.json
    widget_type = data.get('widget_type')
    settings = data.get('settings', '')
    widget = widget_service.add_widget(current_user_id, widget_type, settings)
    return jsonify({
        "id": widget.id,
        "widget_type": widget.widget_type,
        "settings": widget.settings,
        "created_at": widget.created_at
    }), 201

@widget_blueprint.route('/widgets/<int:widget_id>', methods=['DELETE'])
@jwt_required()
def remove_widget(widget_id: int):
    if widget_service.remove_widget(widget_id):
        return '', 204
    return jsonify({"error": "Widget not found"}), 404