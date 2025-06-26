from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import os

before_login_bp = Blueprint('before_login', __name__)

DB_PATH = 'app.db'

# トップページ（ログイン前）
@before_login_bp.route('/', methods=['GET', 'POST'])
def before_login():
    return render_template('before_login.html')


# ログイン処理
@before_login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT id, password FROM users WHERE username = ?", (username,))
        user = c.fetchone()
        conn.close()

        if user and check_password_hash(user[1], password):
            session['user_id'] = user[0]
            flash("ログイン成功")
            return redirect(url_for('after_login.home'))
        else:
            flash("ログイン失敗: ユーザー名またはパスワードが間違っています。")

    return render_template('login.html')


# 新規登録処理
@before_login_bp.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])

        try:
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            flash("登録完了！ログインしてください。")
            return redirect(url_for('before_login.login'))
        except sqlite3.IntegrityError:
            flash("登録失敗: そのユーザー名はすでに使われています。")
        finally:
            conn.close()

    return render_template('registration.html')
