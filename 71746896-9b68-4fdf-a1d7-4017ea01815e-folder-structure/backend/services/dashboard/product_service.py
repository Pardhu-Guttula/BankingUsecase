# Epic Title: Display Tailored Products

from backend.repositories.user.user_repository import UserRepository
from typing import List

class ProductService:
    @staticmethod
    def get_relevant_products(user_profile: dict) -> List[dict]:
        # Epic Title: Display Tailored Products
        products = [
            {'name': 'Premium Credit Card', 'description': 'Exclusive card with premium benefits', 'eligible': user_profile['credit_score'] > 700},
            {'name': 'Personal Loan', 'description': 'Low-interest personal loan', 'eligible': user_profile['income'] > 50000},
            {'name': 'Savings Account', 'description': 'High-interest savings account', 'eligible': True},
        ]

        return [product for product in products if product['eligible']]