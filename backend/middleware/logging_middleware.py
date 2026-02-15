# Epic Title: Consistency Across Devices

import logging
from flask import request

class LoggingMiddleware:
    @staticmethod
    def before_request():
        logging.info('Incoming request: %s %s', request.method, request.path)

    @staticmethod
    def after_request(response):
        logging.info('Outgoing response status: %d', response.status_code)
        return response


# File 6: Implement Consistent Layouts and Register Middleware in app.py