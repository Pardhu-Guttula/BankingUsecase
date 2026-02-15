# Epic Title: Display Tailored Products

from typing import List
from backend.user_dashboard.models.product_model import Product
from backend.user_dashboard.repositories.user_repository import UserRepository

class ProductService:
    @staticmethod
    def get_products_for_user(user) -> List[Product]:
        # Epic Title: Display Tailored Products
        user_profile = UserRepository.get_user_profile(user.id)
        return Product.query.filter_by(profile=user_profile).all()