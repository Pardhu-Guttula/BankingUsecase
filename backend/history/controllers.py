# Epic Title: Maintain Interaction History

from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.history.services import InteractionHistoryService

history_blueprint = Blueprint('history', __name__)
# Initialize InteractionHistoryService later in app.py to inject dependencies
history_service = None  # Placeholder for real instance

@history_blueprint.route('/interactions', methods=['GET'])
@jwt_required()
def get_interactions():
    current_user_id = get_jwt_identity()
    interactions = history_service.get_interaction_history(current_user_id)
    return jsonify([{
        "id": i.id,
        "action": i.action,
        "timestamp": i.timestamp
    } for i in interactions]), 200