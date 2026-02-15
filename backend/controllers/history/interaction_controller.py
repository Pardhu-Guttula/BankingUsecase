# Epic Title: Maintain Interaction History

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.history.interaction_service import InteractionService

interaction_controller = Blueprint('interaction_controller', __name__)

@interaction_controller.route('/history/interactions', methods=['GET'])
@login_required
def get_user_interactions():
    user_id = current_user.id
    interactions = InteractionService.get_interactions_by_user(user_id)
    return jsonify({'interactions': [interaction.serialize() for interaction in interactions]}), 200


# File 5: Schema for Interaction History Table in `database/create_interactions_table.sql`