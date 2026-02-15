# Epic Title: Display Tailored Products

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from backend.services.dashboard.product_service import ProductService

@login_required
def user_dashboard_view(request):
    # Epic Title: Display Tailored Products
    products = ProductService.get_user_relevant_products(request.user)
    return render(request, 'dashboard/product_dashboard.html', {'products': products})