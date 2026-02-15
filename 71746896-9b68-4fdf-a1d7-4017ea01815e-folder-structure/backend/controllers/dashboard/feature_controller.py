# Epic Title: Quick Access to Features

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from backend.services.dashboard.feature_service import FeatureService

@login_required
def feature_dashboard_view(request):
    # Epic Title: Quick Access to Features
    essential_features = FeatureService.get_essential_features()
    return render(request, 'dashboard/feature_dashboard.html', {'essential_features': essential_features})