# Epic Title: Display Tailored Products

from typing import List
from backend.repositories.user.models import UserProfile
from backend.repositories.dashboard.product_repository import ProductRepository

class ProductService:
    @staticmethod
    def get_products_for_profile(profile: UserProfile) -> List[str]:
        # Epic Title: Display Tailored Products
        return ProductRepository.get_products_for_user_profile(profile)