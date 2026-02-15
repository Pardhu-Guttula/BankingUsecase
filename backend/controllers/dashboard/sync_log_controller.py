# Epic Title: Core Banking System Integration

from flask import Blueprint, render_template
from flask_login import login_required
from backend.repositories.core_banking.sync_log_repository import SyncLogRepository

sync_log_controller = Blueprint('sync_log_controller', __name__)

@sync_log_controller.route('/sync_logs', methods=['GET'])
@login_required
def view_sync_logs():
    sync_logs = SyncLogRepository.find_all()
    return render_template('sync_logs.html', sync_logs=sync_logs)


# File 6: Sync Logs Page Template to Display Sync Logs in templates/sync_logs.html