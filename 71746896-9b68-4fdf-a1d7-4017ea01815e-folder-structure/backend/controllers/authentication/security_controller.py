# Epic Title: Secure User Data

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from backend.services.authentication.security_service import SecurityService

@login_required
def encrypt_user_data_view(request):
    # Epic Title: Secure User Data
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        try:
            SecurityService.encrypt_user_data(user_id)
            return HttpResponse("User data encrypted successfully.")
        except Exception as e:
            return HttpResponse(f"Error: {e}", status=500)

    return HttpResponse("Invalid request method", status=405)