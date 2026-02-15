# Epic Title: Display Tailored Products

from django.contrib.auth.models import User
from typing import Dict

class AccountRepository:
    @staticmethod
    def get_account_details(user: User) -> Dict[str, str]:
        # Epic Title: Display Tailored Products
        # Mock account details for the sake of example
        return {'account_type': 'savings', 'balance': '10000'}