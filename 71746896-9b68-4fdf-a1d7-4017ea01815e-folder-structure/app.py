# Epic Title: Quick Access to Features

import logging
import os
from django.core.wsgi import get_wsgi_application
from django.urls import path
from backend.controllers.dashboard.quick_access_dashboard_controller import quick_access_dashboard_view

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()

logger = logging.getLogger('myproject')

def main() -> None:
    # Epic Title: Quick Access to Features
    try:
        logger.info("Starting application...")
        # Place for additional startup code if necessary

    except Exception as e:
        logger.error(f"Error during startup: {e}")
        raise

if __name__ == "__main__":
    main()

urlpatterns = [
    path('quick_access_dashboard/', quick_access_dashboard_view, name='quick_access_dashboard'),
]