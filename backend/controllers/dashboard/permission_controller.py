# Epic Title: Role-based Access Control

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from backend.services.access_control.role_service import RoleService
from backend.forms.permission_form import PermissionForm
from backend.forms.role_permission_form import RolePermissionForm

permission_controller = Blueprint('permission_controller', __name__)

@permission_controller.route('/permissions', methods=['GET'])
@login_required
def list_permissions():
    permissions = RoleService.get_all_permissions()
    return render_template('permissions.html', permissions=permissions)

@permission_controller.route('/permissions/new', methods=['GET', 'POST'])
@login_required
def new_permission():
    form = PermissionForm()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        permission = Permission(name, description)
        PermissionRepository.save(permission)
        return redirect(url_for('permission_controller.list_permissions'))
    return render_template('new_permission.html', form=form)

@permission_controller.route('/roles/assign_permission', methods=['GET', 'POST'])
@login_required
def assign_permission():
    form = RolePermissionForm()
    if form.validate_on_submit():
        role_id = form.roles.data
        permission_id = form.permissions.data
        RoleService.assign_permission_to_role(role_id, permission_id)
        return redirect(url_for('permission_controller.list_permissions'))
    return render_template('assign_permission.html', form=form)


# File 10: Templates to Manage Permissions

## Permissions Template in templates/permissions.html