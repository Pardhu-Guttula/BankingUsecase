# Epic Title: Personalized Dashboard

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from backend.dashboard.services.widget_service import WidgetService

dashboard_controller = Blueprint('dashboard_controller', __name__)

@dashboard_controller.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    widgets = WidgetService.get_widgets_by_user(current_user.id)
    return render_template('dashboard.html', widgets=widgets)

@dashboard_controller.route('/dashboard/add_widget', methods=['POST'])
@login_required
def add_widget():
    name = request.form['name']
    config = request.form['config']
    WidgetService.add_widget(current_user.id, name, config)
    return redirect(url_for('dashboard_controller.dashboard'))

@dashboard_controller.route('/dashboard/remove_widget/<int:widget_id>', methods=['POST'])
@login_required
def remove_widget(widget_id: int):
    WidgetService.remove_widget(widget_id)
    return redirect(url_for('dashboard_controller.dashboard'))


# File 5: Update account/repositories user model to include Widget relationship