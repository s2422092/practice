from flask import Blueprint, render_template, redirect, url_for, session, flash

after_login_bp = Blueprint('after_login', __name__)

# ホーム画面
@after_login_bp.route('/home')
def home():
    if 'user_id' not in session:
        flash("ログインしてください")
        return redirect(url_for('before_login.login'))
    return render_template('home.html')

# ログアウト
@after_login_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("ログアウトしました")
    return redirect(url_for('before_login.before_login'))
