from flask import Blueprint, render_template, redirect,request , url_for , session
import pyotp
from app.models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.check_password(request.form['password']):
            session['mfa_pending'] = user.id
            return redirect(url_for('auth.mfa_verify'))
    return render_template('login.html')

@auth_bp.route('/mfa-verify', methods=['GET', 'POST'])
def mfa_verify():
    if 'mfa_pending' not in session:
        return redirect(url_for('auth.login'))
    
    user = User.query.get(session['mfa_pending'])
    totp = pyotp.TOTP(user.mfa_secret)
    
    if request.method == 'POST' and totp.verify(request.form['code']):
        session['user_id'] = user.id
        return redirect(url_for('dashboard'))
    
    return render_template('mfa_verify.html')