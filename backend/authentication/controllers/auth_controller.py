# Epic Title: Implement Secure Login Mechanism

from flask import Blueprint, request, jsonify, session
from ..services.auth_service import AuthService

auth_controller = Blueprint('auth_controller', __name__)
auth_service = AuthService()

@auth_controller.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    second_factor = request.json.get('second_factor')

    if auth_service.authenticate(username, password, second_factor):
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401



# File 5: Authentication Service in authentication/services/auth_service.py