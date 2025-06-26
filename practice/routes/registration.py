from flask import Blueprint, Flask, render_template, request, redirect, url_for, flash
import sqlite3
from werkzeug.security import generate_password_hash
import os

# Blueprint の定義
registration_bp = Blueprint('registration', __name__)

# 登録ページルート
@registration_bp.route('/registration', methods=['GET', 'POST'])
def registration():
    return render_template('')

app = Flask(__name__)

# データベースにユーザー情報を登録する関数
def insert_user(username, email, password):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
              (username, email, password))
    conn.commit()
    conn.close()

# SQLite データベースを使用してユーザー情報を保存
# /とはじめに表示されるページ
@app.route('/') 
def before_login():
    return render_template('before_login.html')

# ログインページを表示
# /loginとは、ログインページを表示するルート
@app.route('/login')
def login():
    return render_template('login.html')

# ユーザー登録ページを表示
# /registrationとは、ユーザー登録ページを表示するルート
@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        insert_user(username, email, password)
        return redirect(url_for('before_login'))
    return render_template('registration.html')

if __name__ == '__main__':
    app.run(debug=True)
