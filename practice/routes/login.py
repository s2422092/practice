from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import sqlite3
from werkzeug.security import check_password_hash

login_bp = Blueprint('login', __name__, template_folder='templates')

# login_bpのルートURLは /login にします
@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash('ユーザー名とパスワードを入力してください', 'error')
            return redirect(url_for('login.login'))
        
        # データベースからユーザーを検索
        with sqlite3.connect('app.db') as con:
            con.row_factory = sqlite3.Row # カラム名でアクセスできるようにする
            cur = con.cursor()
            cur.execute("SELECT * FROM users WHERE username = ?", (username,))
            user = cur.fetchone()

        # ユーザーが存在し、かつパスワードが一致するかチェック
        if user and check_password_hash(user['password'], password):
            # ログイン成功
            # セッションにユーザー情報を保存
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash(f'ようこそ、{user["username"]}さん', 'success')
            # home.html にリダイレクト
            return redirect(url_for('home.home'))
        else:
            # ログイン失敗
            flash('ユーザー名またはパスワードが正しくありません', 'error')
            return redirect(url_for('login.login'))

    # GETリクエストの場合はログインページを表示
    return render_template('login.html')