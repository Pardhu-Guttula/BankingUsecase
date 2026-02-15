# Epic Title: User Authentication and Security

from flask import session, redirect, url_for
from flask_login import current_user, logout_user
from datetime import datetime, timedelta

class SessionMiddleware:
    @staticmethod
    def before_request():
        session.permanent = True
        session.modified = True
        if current_user.is_authenticated:
            now = datetime.utcnow()
            last_activity = session.get('last_activity')
            if last_activity is None:
                session['last_activity'] = now
            elif now - last_activity > timedelta(minutes=15):
                logout_user()
                return redirect(url_for('authentication_controller.login'))
            else:
                session['last_activity'] = now

    @staticmethod
    def after_request(response):
        return response


# File 2: User Model for Context in models/authentication/user_model.py (Existing File, Re-emitting for Context)