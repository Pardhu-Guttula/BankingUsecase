# Epic Title: Interaction History and Documentation Upload

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from backend.services.interactions.interaction_service import InteractionService

interaction_controller = Blueprint('interaction_controller', __name__)

@interaction_controller.route('/history', methods=['GET'])
@login_required
def view_interaction_history():
    user_id = current_user.id
    interactions = InteractionService.get_interaction_history(user_id)
    return render_template('history.html', interactions=interactions)


# File 6: History Page Template to Display Interaction History in templates/history.html