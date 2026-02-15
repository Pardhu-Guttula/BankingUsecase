# Epic Title: User Authentication and Security

from flask import Blueprint, request, jsonify
from backend.services.authentication.authentication_service import AuthenticationService
from backend.repositories.authentication.user_repository import UserRepository
from flask_login import login_required, current_user

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/user/store_credentials', methods=['POST'])
@login_required
def store_credentials():
    data = request.get_json()
    user = UserRepository.get_user_by_username(current_user.username)
    AuthenticationService.store_user_credentials(user, data['password'])
    return jsonify({"message": "Credentials stored securely"}), 200


# File 7: Update requirements.txt with Only Necessary Dependencies