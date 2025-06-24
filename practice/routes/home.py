from flask import Blueprint, render_template, redirect, url_for, flash, session

home_bp = Blueprint('home', __name__, template_folder='templates')

@home_bp.route('/home')
def home():
    # セッションに 'username' が存在するかチェック（ログイン状態か確認）
    if 'username' in session:
        # セッションからユーザー名を取得
        username = session['username']
        # ユーザー名を渡してhome.htmlを表示
        return render_template('home.html', username=username)
    else:
        # ログインしていない場合は、ログインページにリダイレクト
        flash('ログインしてください', 'error')
        return redirect(url_for('login.login'))