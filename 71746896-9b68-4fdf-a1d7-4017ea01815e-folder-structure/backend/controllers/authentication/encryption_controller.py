# Epic Title: Secure User Data

from django.http import JsonResponse, HttpRequest
from django.contrib.auth import get_user_model
from backend.services.authentication.encryption_service import EncryptionService
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def store_user_data(request: HttpRequest) -> JsonResponse:
    # Epic Title: Secure User Data
    if request.method == 'POST':
        username = request.POST['username']
        raw_password = request.POST['password']
        encrypted_data = EncryptionService.encrypt_data(raw_password)
        hashed_password = EncryptionService.hash_password(raw_password)

        user_model = get_user_model()
        user = user_model.objects.create(username=username, password=hashed_password, encrypted_data=encrypted_data)
        return JsonResponse({"message": "User data stored securely"}, status=201)

    return JsonResponse({"message": "Invalid request method"}, status=405)