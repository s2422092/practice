from flask import Blueprint, render_template, request, redirect, url_for, flash
import sqlite3
from werkzeug.security import generate_password_hash

# Blueprint の定義
registration_bp = Blueprint('registration', __name__, template_folder='templates')

# 登録ページルート
@registration_bp.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        # フォームからデータを取得
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash('ユーザー名とパスワードを入力してください', 'error')
            return redirect(url_for('registration.registration'))

        # パスワードをハッシュ化
        hashed_password = generate_password_hash(password)
        
        # データベースに接続
        # "with" を使うと自動で接続を閉じてくれるので安全
        try:
            with sqlite3.connect('app.db') as con:
                cur = con.cursor()
                # ユーザーをDBに挿入
                cur.execute(
                    "INSERT INTO users (username, password) VALUES (?, ?)",
                    (username, hashed_password)
                )
                con.commit()
            flash('登録が完了しました。ログインしてください。', 'success')
            # 登録完了後、ログイン前のトップページにリダイレクト
            return redirect(url_for('before_login.before_login'))
        except sqlite3.IntegrityError:
            # ユーザー名が重複していた場合
            flash('そのユーザー名は既に使用されています。', 'error')
            return redirect(url_for('registration.registration'))

    # GETリクエストの場合は登録ページを表示
    return render_template('registration.html')