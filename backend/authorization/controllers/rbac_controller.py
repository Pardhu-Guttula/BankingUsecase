# Epic Title: Role-Based Access Control

from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from backend.authorization.services.rbac_service import RBACService
from backend.authorization.models.role_model import Role
from backend.authorization.models.user_role_model import UserRole

rbac_bp = Blueprint('rbac', __name__)

@rbac_bp.route('/assign_role', methods=['GET', 'POST'])
@login_required
def assign_role():
    # Epic Title: Role-Based Access Control
    if request.method == 'POST':
        user_id = request.form['user_id']
        role_id = request.form['role_id']
        RBACService.assign_role_to_user(user_id, role_id)
        flash('Role assigned successfully')
        return redirect(url_for('rbac.assign_role'))
    
    roles = Role.query.all()
    return render_template('assign_role.html', roles=roles, current_user=current_user)

@rbac_bp.route('/admin_resource')
@login_required
@RBACService.role_required('admin')
def admin_resource():
    # Epic Title: Role-Based Access Control
    return "This is an admin resource, only accessible by users with the 'admin' role."