# Epic Title: Secure User Data

from flask import Blueprint, request, redirect, url_for, flash, render_template
from werkzeug.security import check_password_hash
from flask_login import login_user, current_user, login_required, logout_user
from backend.authentication.repositories.user_repository import UserRepository
from backend.authentication.services.encryption_service import EncryptionService

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    # Epic Title: Secure User Data
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        mobile = request.form['mobile']
        UserRepository.add_user(email, password, mobile)
        flash('User registered successfully!', 'success')
        return redirect(url_for('user.login'))
    return render_template('register.html')

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Epic Title: Secure User Data
    if request.method == 'POST':
        user = UserRepository.find_by_email(request.form['email'])
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('dashboard'))
        flash('Invalid email or password', 'danger')
    return render_template('login.html')

@user_bp.route('/logout')
@login_required
def logout():
    # Epic Title: Secure User Data
    logout_user()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('user.login'))