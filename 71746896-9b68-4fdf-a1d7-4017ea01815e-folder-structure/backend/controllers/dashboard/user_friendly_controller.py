# Epic Title: User-Friendly Interface

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def user_friendly_dashboard_view(request):
    # Epic Title: User-Friendly Interface
    return render(request, 'dashboard/user_friendly_dashboard.html')