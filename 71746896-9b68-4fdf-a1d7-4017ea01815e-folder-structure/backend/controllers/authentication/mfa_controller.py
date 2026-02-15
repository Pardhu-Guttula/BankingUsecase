# Epic Title: Implement Multi-Factor Authentication

from django.http import JsonResponse, HttpRequest
from django.contrib.auth import authenticate
from backend.services.authentication.mfa_service import MFAService

def prompt_for_second_factor(request: HttpRequest) -> JsonResponse:
    # Epic Title: Implement Multi-Factor Authentication
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        if MFAService.has_second_factor(user):
            MFAService.send_second_factor_code(user)
            return JsonResponse({"message": "Second factor required"}, status=200)
        else:
            return JsonResponse({"message": "Second factor not registered"}, status=400)
    return JsonResponse({"message": "Invalid credentials"}, status=401)

def verify_second_factor(request: HttpRequest) -> JsonResponse:
    # Epic Title: Implement Multi-Factor Authentication
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is not None and MFAService.check_code(user, request.POST['code']):
        return JsonResponse({"message": "Authentication successful"}, status=200)
    return JsonResponse({"message": "Invalid second factor"}, status=401)