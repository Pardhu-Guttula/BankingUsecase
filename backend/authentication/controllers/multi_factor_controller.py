# Epic Title: Implement Multi-Factor Authentication

from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, current_user, login_required
from werkzeug.security import check_password_hash
from backend.authentication.services.multi_factor_service import send_otp, verify_otp
from backend.authentication.repositories.user_repository import UserRepository

multi_factor_bp = Blueprint('multi_factor', __name__)

@multi_factor_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Epic Title: Implement Multi-Factor Authentication
    if request.method == 'POST':
        user = UserRepository.find_by_email(request.form['email'])
        if user and check_password_hash(user.password, request.form['password']):
            send_otp(user)
            flash('An OTP has been sent to your registered mobile device.', 'info')
            return redirect(url_for('multi_factor.verify_otp', user_id=user.id))
        flash('Invalid email or password', 'danger')
    return render_template('login.html')

@multi_factor_bp.route('/verify_otp/<int:user_id>', methods=['GET', 'POST'])
def verify_otp_route(user_id):
    # Epic Title: Implement Multi-Factor Authentication
    if request.method == 'POST':
        if verify_otp(user_id, request.form['otp']):
            user = UserRepository.find_by_id(user_id)
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('dashboard'))
        flash('Invalid OTP', 'danger')
    return render_template('verify_otp.html')