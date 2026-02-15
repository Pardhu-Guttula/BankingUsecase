# Epic Title: Display Tailored Products

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from backend.user_dashboard.services.product_service import ProductService

product_dashboard_bp = Blueprint('product_dashboard', __name__)

@product_dashboard_bp.route('/dashboard')
@login_required
def dashboard():
    # Epic Title: Display Tailored Products
    user_products = ProductService.get_products_for_user(current_user)
    return render_template('product_dashboard.html', products=user_products)