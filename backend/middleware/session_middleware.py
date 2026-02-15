# Epic Title: User Authentication and Security

from flask import Flask, request, redirect, url_for
from flask_login import current_user
from backend.auth.services.authentication_service import AuthenticationService

def session_expiry_middleware(app: Flask):
    @app.before_request
    def before_request():
        if current_user.is_authenticated:
            if AuthenticationService.check_session_expiry():
                return redirect(url_for('auth_controller.login'))


# File 5: Update Main App to Include Session Expiry Middleware in app.py