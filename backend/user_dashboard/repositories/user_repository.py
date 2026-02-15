# Epic Title: Display Tailored Products

from backend.user_dashboard.models.user_model import User

class UserRepository:
    @staticmethod
    def get_user_profile(user_id: int) -> str:
        # Epic Title: Display Tailored Products
        user = User.query.get(user_id)
        return user.profile if user else None