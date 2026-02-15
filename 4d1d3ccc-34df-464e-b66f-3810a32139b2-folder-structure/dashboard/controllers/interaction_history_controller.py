# Epic Title: Interaction History and Documentation Upload

from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from dashboard.services.interaction_history_service import InteractionHistoryService

interaction_history_controller = Blueprint('interaction_history_controller', __name__)

@interaction_history_controller.route('/interactions', methods=['GET'])
@login_required
def get_interactions():
    interactions = InteractionHistoryService.get_user_interactions(current_user.id)
    return jsonify(interactions), 200


# File 5: App Update to Register Interaction History Controller in app.py