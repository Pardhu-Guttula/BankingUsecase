# Epic Title: Display Tailored Products

from django.contrib.auth.models import User
from backend.repositories.user.user_repository import UserRepository
from backend.repositories.accounts.account_repository import AccountRepository
from typing import List, Dict

class ProductService:

    @staticmethod
    def get_user_relevant_products(user: User) -> List[Dict[str, str]]:
        # Epic Title: Display Tailored Products
        user_profile = UserRepository.get_profile(user)
        account_details = AccountRepository.get_account_details(user)

        products = [
            {'name': 'Premium Savings Account', 'eligibility': 'High Net-Worth Individuals'},
            {'name': 'Personal Loan', 'eligibility': 'Salaried Employees'},
            # more products based on mock data for now
        ]

        relevant_products = [product for product in products if product['eligibility'] in user_profile['tags']]

        return relevant_products