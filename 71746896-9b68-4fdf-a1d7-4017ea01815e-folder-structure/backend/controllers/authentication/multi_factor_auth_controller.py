# Epic Title: Implement Multi-Factor Authentication

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.conf import settings
from backend.services.authentication.mfa_service import MFAService

def login_view(request):
    # Epic Title: Implement Multi-Factor Authentication
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            request.session['pre_mfa_user_id'] = user.id
            request.session['pre_mfa_username'] = username
            request.session['pre_mfa_password'] = password
            return redirect('mfa_verify')
        else:
            return render(request, 'authentication/login.html', {'error': 'Invalid credentials'})

    return render(request, 'authentication/login.html')

@login_required
def mfa_verify_view(request):
    # Epic Title: Implement Multi-Factor Authentication
    if request.method == 'POST':
        token = request.POST['token']
        user_id = request.session.get('pre_mfa_user_id')
        username = request.session.get('pre_mfa_username')
        password = request.session.get('pre_mfa_password')

        if MFAService.verify_token(user_id, token):
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'authentication/mfa_verify.html', {'error': 'Authentication failed'})
        else:
            return render(request, 'authentication/mfa_verify.html', {'error': 'Invalid token'})

    return render(request, 'authentication/mfa_verify.html')