# Epic Title: Quick Access to Features

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def quick_access_dashboard_view(request):
    # Epic Title: Quick Access to Features
    return render(request, 'dashboard/quick_access_dashboard.html')