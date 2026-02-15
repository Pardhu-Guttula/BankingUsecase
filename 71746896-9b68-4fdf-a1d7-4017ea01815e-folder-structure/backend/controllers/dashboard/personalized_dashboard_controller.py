# Epic Title: Display Tailored Products

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from backend.services.dashboard.product_service import ProductService

@login_required
def personalized_dashboard_view(request):
    # Epic Title: Display Tailored Products
    user_profile = request.user.profile
    products = ProductService.get_relevant_products(user_profile)
    return render(request, 'dashboard/personalized_dashboard.html', {'products': products})