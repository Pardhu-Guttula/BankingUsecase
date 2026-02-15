# Epic Title: Responsive User Interface

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def responsive_dashboard_view(request):
    # Epic Title: Responsive User Interface
    return render(request, 'dashboard/responsive_dashboard.html')