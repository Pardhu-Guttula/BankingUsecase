# Epic Title: Display Tailored Products

from typing import List
from backend.repositories.user.models import UserProfile

class ProductRepository:
    @staticmethod
    def get_products_for_user_profile(profile: UserProfile) -> List[str]:
        # Epic Title: Display Tailored Products
        # This function should return a list of product names based on the user profile.
        # Implement actual logic to fetch products relevant to the profile
        # For demonstration, returning a static list
        return ["Product1", "Product2", "Product3"]