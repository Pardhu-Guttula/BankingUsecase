# Epic Title: Personalized Dashboard

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.dashboard.services import DashboardService

dashboard_blueprint = Blueprint('dashboard', __name__)
# Initialize DashboardService later in app.py to inject dependencies
dashboard_service = None  # Placeholder for real instance

@dashboard_blueprint.route('/dashboard', methods=['GET'])
@jwt_required()
def get_dashboard():
    current_user_id = get_jwt_identity()
    data = dashboard_service.get_dashboard_data(current_user_id)
    return jsonify(data), 200

@dashboard_blueprint.route('/dashboard/widgets', methods=['POST'])
@jwt_required()
def add_widget():
    current_user_id = get_jwt_identity()
    widget_name = request.json.get('name')
    config = request.json.get('config')
    if not widget_name:
        return jsonify({"error": "Widget name is required"}), 400

    widget = dashboard_service.add_widget_for_user(current_user_id, widget_name, config)
    return jsonify({"message": "Widget added successfully", "widget": {"id": widget.id, "name": widget.name, "config": widget.config}}), 201

@dashboard_blueprint.route('/dashboard/widgets/<int:widget_id>', methods=['DELETE'])
@jwt_required()
def remove_widget(widget_id):
    current_user_id = get_jwt_identity()
    dashboard_service.remove_widget_for_user(current_user_id, widget_id)
    return jsonify({"message": "Widget removed successfully"}), 200

@dashboard_blueprint.route('/dashboard/summary', methods=['GET'])
@jwt_required()
def get_financial_summary():
    current_user_id = get_jwt_identity()
    summary = dashboard_service.get_financial_summary(current_user_id)
    return jsonify(summary), 200