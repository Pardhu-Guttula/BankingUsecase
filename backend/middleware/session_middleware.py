# Epic Title: User Authentication and Security

from flask import session, redirect, url_for
from datetime import timedelta

class SessionMiddleware:
    @staticmethod
    def before_request():
        session.permanent = True
        # Each user session time limit initiated
        session.permanent_session_lifetime = timedelta(minutes=15)
        session.modified = True

        if session.get('last_activity'):
            now = datetime.utcnow()
            duration = now - session['last_activity']
            if duration.total_seconds() > 900:  # 15 minutes in seconds
                session.clear()
                return redirect(url_for('authentication_controller.logout'))

        session['last_activity'] = datetime.utcnow()

    @staticmethod
    def after_request(response):
        session.modified = True
        return response


# File 2: Session Management Update in app.py to include Session Middleware before and after request