from flask import Blueprint, render_template
from flask_login import login_required
from app.auth import role_required

main_bp = Blueprint('main', __name__)

@main_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@main_bp.route('/admin')
@role_required('admin')
def admin_panel():
    return render_template('admin.html')