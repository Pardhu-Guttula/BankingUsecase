# Epic Title: Consistent User Experience

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def consistent_navigation_view(request):
    # Epic Title: Consistent User Experience
    return render(request, 'dashboard/consistent_navigation.html')