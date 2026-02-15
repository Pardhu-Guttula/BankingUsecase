# Epic Title: Display Tailored Products

import logging
import os
from django.core.wsgi import get_wsgi_application
from django.urls import path
from backend.controllers.dashboard.personalized_dashboard_controller import personalized_dashboard_view

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()

logger = logging.getLogger('myproject')

def main() -> None:
    # Epic Title: Display Tailored Products
    try:
        logger.info("Starting application...")
        # Place for additional startup code if necessary

    except Exception as e:
        logger.error(f"Error during startup: {e}")
        raise

if __name__ == "__main__":
    main()

urlpatterns = [
    path('personalized_dashboard/', personalized_dashboard_view, name='personalized_dashboard'),
]