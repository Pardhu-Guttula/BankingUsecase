# Epic Title: Secure User Data

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from backend.services.authentication.encryption_service import EncryptionService
from backend.services.authentication.hashing_service import HashingService

@login_required
def update_password_view(request):
    # Epic Title: Secure User Data
    if request.method == 'POST':
        new_password = request.POST['new_password']
        hashed_password = HashingService.hash_password(new_password)
        user = request.user
        user.password = hashed_password
        user.save()
        return render(request, 'authentication/update_password_success.html')

    return render(request, 'authentication/update_password.html')