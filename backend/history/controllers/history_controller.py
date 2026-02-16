# Epic Title: Interaction History and Documentation Upload

from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.history.services.interaction_service import InteractionService

history_blueprint = Blueprint('history', __name__)
interaction_service = InteractionService()

@history_blueprint.route('/interaction-history', methods=['GET'])
@jwt_required()
def get_interaction_history():
    user_id = get_jwt_identity()
    history = interaction_service.get_interaction_history(user_id)
    return jsonify([{
        "id": h.id,
        "action": h.action,
        "timestamp": h.timestamp
    } for h in history]), 200