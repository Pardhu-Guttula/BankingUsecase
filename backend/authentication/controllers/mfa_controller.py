# Epic Title: Implement Multi-Factor Authentication

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, current_user
from backend.authentication.models.user_model import User
from backend.authentication.services.mfa_service import MFAService

mfa_bp = Blueprint('mfa', __name__)

@mfa_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Epic Title: Implement Multi-Factor Authentication
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            login_user(user)
            MFAService.send_mfa_code(user)
            return redirect(url_for('mfa.verify_mfa'))
        
        flash('Invalid email or password')
    
    return render_template('login.html')

@mfa_bp.route('/verify_mfa', methods=['GET', 'POST'])
def verify_mfa():
    # Epic Title: Implement Multi-Factor Authentication
    if request.method == 'POST':
        mfa_code = request.form['mfa_code']
        if MFAService.verify_mfa_code(current_user, mfa_code):
            flash('Authentication successful')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid MFA code')
    
    return render_template('verify_mfa.html')