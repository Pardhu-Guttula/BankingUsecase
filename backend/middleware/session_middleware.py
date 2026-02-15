# Epic Title: User Authentication and Security

from flask import session
from datetime import datetime, timedelta
from flask import current_app
from flask_login import logout_user

class SessionMiddleware:
    @staticmethod
    def before_request():
        now = datetime.utcnow()
        session.permanent = True
        current_app.permanent_session_lifetime = timedelta(minutes=15)
        session.modified = True
        
        if 'last_activity' in session:
            last_activity = session['last_activity']
            if now - last_activity > current_app.permanent_session_lifetime:
                logout_user()
                session.clear()
        session['last_activity'] = now

    @staticmethod
    def after_request(response):
        session.modified = True
        return response


# File 2: Update Main App to Use Session Middleware in app.py