# Epic Title: Maintain Interaction History

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.interaction_history.services.interaction_service import InteractionService

interaction_controller = Blueprint('interaction_controller', __name__)

@interaction_controller.route('/history', methods=['GET'])
@login_required
def get_history():
    user_id = current_user.id
    interactions = InteractionService.get_user_interactions(user_id)
    interaction_list = [{"id": i.id, "action": i.action, "timestamp": i.timestamp} for i in interactions]
    return jsonify(interaction_list)


# File 5: Interaction History Template in user_dashboard/templates/history.html