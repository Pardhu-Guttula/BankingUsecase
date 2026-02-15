# Epic Title: Role-Based Access Control

from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from backend.authorization.services.role_service import RoleService
from backend.authorization.repositories.user_repository import UserRepository

role_bp = Blueprint('role', __name__)

@role_bp.route('/assign_role', methods=['GET', 'POST'])
@login_required
def assign_role():
    # Epic Title: Role-Based Access Control
    if not current_user.is_admin:
        flash('Access denied', 'danger')
        return redirect(url_for('index'))

    if request.method == 'POST':
        user = UserRepository.find_by_email(request.form['email'])
        role = request.form['role']
        if user:
            RoleService.assign_role(user, role)
            flash('Role assigned successfully', 'success')
        else:
            flash('User not found', 'danger')
    return render_template('assign_role.html')

@role_bp.route('/restricted_resource')
@login_required
def restricted_resource():
    # Epic Title: Role-Based Access Control
    if not RoleService.has_role(current_user, 'admin'):
        flash('Access denied', 'danger')
        return redirect(url_for('index'))
    return render_template('restricted_resource.html')