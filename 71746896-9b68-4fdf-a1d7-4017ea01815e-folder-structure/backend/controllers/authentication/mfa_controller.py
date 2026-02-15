# Epic Title: Implement Multi-Factor Authentication

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from backend.services.authentication.mfa_service import MFAService

def login_view(request):
    # Epic Title: Implement Multi-Factor Authentication
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            request.session['pre_auth_user_id'] = user.id
            return redirect('mfa_prompt')
    
    return render(request, 'authentication/login.html')

@login_required
def mfa_prompt_view(request):
    # Epic Title: Implement Multi-Factor Authentication
    if request.method == "POST":
        code = request.POST.get('code')
        user_id = request.session.get('pre_auth_user_id')
        if not user_id:
            return HttpResponse("Session expired", status=403)
        
        if MFAService.verify_code(user_id, code):
            user = authenticate(user_id=user_id)
            login(request, user)
            return redirect('dashboard')

        return HttpResponse("Invalid code", status=403)

    return render(request, 'authentication/mfa_prompt.html')