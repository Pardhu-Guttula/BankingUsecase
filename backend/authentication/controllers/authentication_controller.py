# Epic Title: User Authentication and Security

from flask import Blueprint, request, jsonify
from backend.authentication.repositories.user_repository import UserRepository

authentication_controller = Blueprint('authentication_controller', __name__)

@authentication_controller.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if not username or not password or not email:
        return jsonify({"message": "Username, password and email are required"}), 400

    if UserRepository.get_user_by_username(username):
        return jsonify({"message": "Username already exists"}), 409

    user = UserRepository.create_user(username, password, email)
    return jsonify({"message": "User registered successfully", "user_id": user.id}), 201


# File 4: Update Main App to Register Authentication Controller in app.py