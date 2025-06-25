from flask import Blueprint, render_template, request, redirect, url_for, flash
import sqlite3
from werkzeug.security import generate_password_hash
import os

# Blueprint の定義
before_login_bp = Blueprint('before_login', __name__)
#　before_login_bpは、アプリケーションのルーティングを管理するためのBlueprintです。
# Blueprint('before_login', __name__)は、'before_login'という名前のBlueprintを作成し、__name__を使って現在のモジュールを識別します。
# nameは、Blueprintの名前であり、__name__は現在のモジュールの名前を示します。

# 登録ページルート
@before_login_bp.route('/', methods=['GET', 'POST'])
def before_login():
    
    return render_template('before_login.html')

# このファイルは何をしているのかというと、
# 1. FlaskのBlueprintを使って、アプリケーションのルーティングを管理しています。
# 2. 登録ページのルートを定義し、GETリクエストで登録ページを表示し、POSTリクエストでユーザー登録を処理します。
# 3. SQLiteデータベースに接続し、ユーザー情報を保存します。
# 4. 登録が成功した場合は、ログインページにリダイレクトし、失敗した場合はエラーメッセージを表示します。

# ルートとは、アプリケーション内の特定のURLパスに関連付けられた処理のことです。それをすることで、ユーザーが特定のURLにアクセスしたときに、どの処理を実行するかを決定します。