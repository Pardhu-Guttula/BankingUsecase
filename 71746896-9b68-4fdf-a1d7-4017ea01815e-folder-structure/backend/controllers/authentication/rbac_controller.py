# Epic Title: Role-Based Access Control

from django.http import JsonResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from backend.services.authentication.rbac_service import RBACService

@login_required
def assign_role_to_user(request: HttpRequest) -> JsonResponse:
    # Epic Title: Role-Based Access Control
    if request.user.is_staff:
        username = request.POST['username']
        role_name = request.POST['role_name']
        if RBACService.assign_role(username, role_name):
            return JsonResponse({"message": "Role assigned successfully"}, status=200)
        else:
            return JsonResponse({"message": "Failed to assign role"}, status=400)
    return JsonResponse({"message": "Unauthorized"}, status=403)

@login_required
def check_access(request: HttpRequest) -> JsonResponse:
    # Epic Title: Role-Based Access Control
    resource = request.POST['resource']
    if RBACService.has_access(request.user, resource):
        return JsonResponse({"message": "Access granted"}, status=200)
    return JsonResponse({"message": "Access denied"}, status=403)