# Epic Title: User Authentication and Security

from flask import redirect, url_for, session
from flask_login import current_user

class SessionMiddleware:
    @staticmethod
    def before_request():
        if current_user.is_authenticated and session.get('2fa_required'):
            return redirect(url_for('authentication_controller.verify_2fa'))

    @staticmethod
    def after_request(response):
        session.permanent = True
        return response


# File 6: Update Main App to Register Authentication Controller in app.py