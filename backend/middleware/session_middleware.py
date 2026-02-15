# Epic Title: User Authentication and Security

from flask import session, redirect, url_for
from datetime import timedelta, datetime

class SessionMiddleware:
    
    @staticmethod
    def before_request():
        session.permanent = True
        app.permanent_session_lifetime = timedelta(minutes=15)
        session.modified = True
        if 'last_activity' in session:
            now = datetime.utcnow()
            last_activity = session['last_activity']
            if now - last_activity > app.permanent_session_lifetime:
                session.clear()
                return redirect(url_for('authentication_controller.login'))
        session['last_activity'] = datetime.utcnow()

    @staticmethod
    def after_request(response):
        session.modified = True
        return response

# File 2: User Model in models/authentication/user_model.py (Already exists, Modified)