# Epic Title: Adaptive Screen Resolutions

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def adaptive_resolution_view(request):
    # Epic Title: Adaptive Screen Resolutions
    return render(request, 'dashboard/adaptive_resolution.html')