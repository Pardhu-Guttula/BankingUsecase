# Epic Title: Create Secure User Sessions

from flask import session, redirect, url_for, request
from datetime import datetime, timedelta
from flask_login import current_user, logout_user

class SessionMiddleware:
    @staticmethod
    def before_request():
        session.permanent = True
        app.permanent_session_lifetime = timedelta(minutes=15)
        
        if 'last_activity' in session:
            now = int(datetime.utcnow().timestamp())
            if now - session['last_activity'] > 15 * 60:
                session.clear()
                if current_user.is_authenticated:
                    logout_user()
                return redirect(url_for('authentication_controller.login', next=request.url))
        session['last_activity'] = int(datetime.utcnow().timestamp())

    @staticmethod
    def after_request(response):
        session.modified = True
        return response


# File 2: Authentication Controller Updated for Session Handling in controllers/authentication/authentication_controller.py