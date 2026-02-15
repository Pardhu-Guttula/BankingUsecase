# Epic Title: User Authentication and Security

from flask import Blueprint, request, jsonify
from backend.services.authentication.user_service import UserService

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    user = UserService.create_user(username, email, password)

    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email
    }), 201

@user_controller.route('/verify-password', methods=['POST'])
def verify_password():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = UserRepository.get_by_username(username)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    if UserService.verify_password(password, user.password_hash):
        return jsonify({'message': 'Password is valid'}), 200
    else:
        return jsonify({'message': 'Invalid password'}), 401

# File 5: Register User Controller Blueprint in app.py (Already Exists, Modified)