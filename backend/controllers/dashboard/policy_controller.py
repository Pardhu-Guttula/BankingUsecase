# Epic Title: Role-based Access Control

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from backend.services.access_control.policy_service import PolicyService
from backend.forms.policy_form import PolicyForm

policy_controller = Blueprint('policy_controller', __name__)

@policy_controller.route('/policies', methods=['GET'])
@login_required
def list_policies():
    policies = PolicyService.get_all_policies()
    return render_template('policies.html', policies=policies)

@policy_controller.route('/policies/new', methods=['GET', 'POST'])
@login_required
def new_policy():
    form = PolicyForm()
    if form.validate_on_submit():
        role_id = form.role_id.data
        service_name = form.service_name.data
        access_level = form.access_level.data
        PolicyService.create_policy(role_id, service_name, access_level)
        return redirect(url_for('policy_controller.list_policies'))
    return render_template('new_policy.html', form=form)


# File 7: Templates to Manage Policies

## Policies Template in templates/policies.html