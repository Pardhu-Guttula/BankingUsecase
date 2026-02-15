# Epic Title: Role-Based Access Control

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from backend.services.authentication.role_service import RoleService

@login_required
@user_passes_test(lambda u: u.is_superuser)
def assign_role_view(request):
    # Epic Title: Role-Based Access Control
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        role = request.POST.get('role')
        RoleService.assign_role(user_id, role)
        return redirect('assign_role_success')

    users = User.objects.all()
    roles = RoleService.get_all_roles()
    return render(request, 'authentication/assign_role.html', {'users': users, 'roles': roles})