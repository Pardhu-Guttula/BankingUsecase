# Epic Title: Interaction History and Documentation Upload

from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from backend.services.interactions.interaction_history_service import InteractionHistoryService

interaction_history_controller = Blueprint('interaction_history_controller', __name__)

@interaction_history_controller.route('/interactions', methods=['GET'])
@login_required
def get_interactions():
    interactions = InteractionHistoryService.get_user_interactions(current_user.id)
    interactions_list = [{
        'id': i.id,
        'user_id': i.user_id,
        'action': i.action,
        'timestamp': i.timestamp
    } for i in interactions]
    return jsonify(interactions_list)

# File 5: Register Interaction History Controller Blueprint in app.py (Already Exists, Modified)