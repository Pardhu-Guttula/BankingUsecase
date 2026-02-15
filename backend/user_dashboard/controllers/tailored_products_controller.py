# Epic Title: Display Tailored Products

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from backend.user_dashboard.services.product_service import ProductService

tailored_products_bp = Blueprint('tailored_products', __name__)

@tailored_products_bp.route('/tailored-dashboard')
@login_required
def dashboard():
    # Epic Title: Display Tailored Products
    user_profile = current_user.profile  # Assume 'profile' is a field in the User model
    tailored_products = ProductService.get_products_for_profile(user_profile)
    return render_template('tailored_dashboard.html', products=tailored_products)