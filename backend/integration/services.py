# Epic Title: Core Banking System Integration

import logging
import requests
from werkzeug.exceptions import BadRequest, InternalServerError
from requests.auth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
from backend.integration.models import CoreBankingIntegration

logger = logging.getLogger(__name__)

class CoreBankingService:
    def __init__(self, db: SQLAlchemy, base_url: str, auth: HTTPBasicAuth):
        self.db = db
        self.base_url = base_url
        self.auth = auth

    def log_interaction(self, request_details: str, response_details: str, status_code: int):
        integration_log = CoreBankingIntegration(
            request_details=request_details, 
            response_details=response_details, 
            status_code=status_code
        )
        self.db.session.add(integration_log)
        self.db.session.commit()
        logger.info(f"Logged integration interaction: {integration_log}")

    def make_request(self, endpoint: str, method: str = 'GET', data: dict = None) -> dict:
        url = f"{self.base_url}{endpoint}"
        try:
            logger.info(f"Making request to Core Banking System at {url}")
            if method == 'GET':
                response = requests.get(url, auth=self.auth)
            else:
                response = requests.post(url, json=data, auth=self.auth)

            self.log_interaction(request_details=str(data), response_details=response.text, status_code=response.status_code)

            if response.status_code != 200:
                logger.error(f"Error from Core Banking System: {response.status_code} - {response.text}")
                raise InternalServerError(description="Error from Core Banking System")

            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Request to Core Banking System failed: {e}")
            raise BadRequest(description="Request to Core Banking System failed")