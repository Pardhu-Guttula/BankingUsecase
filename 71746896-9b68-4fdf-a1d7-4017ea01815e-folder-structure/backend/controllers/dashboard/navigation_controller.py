# Epic Title: User-Friendly Interface

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from backend.services.dashboard.navigation_service import NavigationService

@login_required
def navigation_view(request):
    # Epic Title: User-Friendly Interface
    navigation_items = NavigationService.get_navigation_items()
    essential_features = NavigationService.get_essential_features()
    return render(request, 'dashboard/navigation.html', {'navigation_items': navigation_items, 'essential_features': essential_features})