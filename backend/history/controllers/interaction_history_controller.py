# Epic Title: Interaction History and Documentation Upload

from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from backend.services.interactions.interaction_history_service import InteractionHistoryService

interaction_history_controller = Blueprint('interaction_history_controller', __name__)

@interaction_history_controller.route('/user/history', methods=['GET'])
@login_required
def get_user_history():
    history = InteractionHistoryService.get_user_history(current_user.id)
    history_data = [{
        "id": h.id,
        "action": h.action,
        "timestamp": h.timestamp
    } for h in history]
    return jsonify(history_data), 200


# File 6: Update Main App to Register Interaction History Controller in app.py