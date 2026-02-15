# Epic Title: Role-Based Access Control

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from backend.services.authentication.role_service import RoleService

@login_required
@user_passes_test(lambda u: RoleService.has_role(u, 'admin'))
def admin_dashboard_view(request):
    # Epic Title: Role-Based Access Control
    return render(request, 'authentication/admin_dashboard.html')

@login_required
@user_passes_test(lambda u: RoleService.has_role(u, 'user'))
def user_dashboard_view(request):
    # Epic Title: Role-Based Access Control
    return render(request, 'authentication/user_dashboard.html')