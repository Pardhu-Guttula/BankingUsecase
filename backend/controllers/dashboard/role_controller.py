# Epic Title: Role-based Access Control

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from backend.services.access_control.role_service import RoleService
from backend.forms.role_form import RoleForm

role_controller = Blueprint('role_controller', __name__)

@role_controller.route('/roles', methods=['GET'])
@login_required
def list_roles():
    roles = RoleService.get_all_roles()
    return render_template('roles.html', roles=roles)

@role_controller.route('/roles/new', methods=['GET', 'POST'])
@login_required
def new_role():
    form = RoleForm()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        RoleService.create_role(name, description)
        return redirect(url_for('role_controller.list_roles'))
    return render_template('new_role.html', form=form)


# File 8: Templates to Manage Roles

## Roles Template in templates/roles.html