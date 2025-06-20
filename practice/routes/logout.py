from flask import session, redirect, url_for, Blueprint
from flask import render_template

logout_bp = Blueprint('auth', __name__)

@logout_bp.route('/logout')
def logout():
    return render_template('')