# Epic Title: Display Tailored Products

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from backend.services.dashboard.product_service import ProductService

@login_required
def personalized_dashboard_view(request):
    # Epic Title: Display Tailored Products
    user_profile = request.user.profile
    tailored_products = ProductService.get_products_for_profile(user_profile)
    return render(request, 'dashboard/personalized_dashboard.html', {'products': tailored_products})