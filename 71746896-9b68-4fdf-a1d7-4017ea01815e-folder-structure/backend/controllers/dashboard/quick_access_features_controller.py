# Epic Title: Quick Access to Features

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def quick_access_features_view(request):
    # Epic Title: Quick Access to Features
    key_features = [
        {'name': 'Manage Accounts', 'url': '/accounts/'},
        {'name': 'Transfer Funds', 'url': '/transfer/'},
        {'name': 'Pay Bills', 'url': '/pay_bills/'},
        {'name': 'Investment Options', 'url': '/investments/'},
    ]
    return render(request, 'dashboard/quick_access_features.html', {'key_features': key_features})