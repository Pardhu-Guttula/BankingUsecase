# Epic Title: Interaction History and Documentation Upload

from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from backend.history.services.interaction_service import InteractionService

interaction_controller = Blueprint('interaction_controller', __name__)

@interaction_controller.route('/interactions', methods=['GET'])
@login_required
def get_interactions():
    interactions = InteractionService.get_user_interactions(current_user.id)
    return jsonify([{
        "id": interaction.id,
        "action": interaction.action,
        "details": interaction.details,
        "timestamp": interaction.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    } for interaction in interactions])


# File 5: Update Main App to Register Interaction Controller in app.py