# Epic Title: Display Tailored Products

from typing import List
from backend.user_dashboard.models.product_model import Product

class ProductService:
    @staticmethod
    def get_products_for_profile(profile: str) -> List[Product]:
        # Epic Title: Display Tailored Products
        # Simulate a query based on user profile
        products = Product.query.filter_by(profile_criteria=profile).all()
        return products