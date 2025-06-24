from flask import Flask
# ... 他の必要なimport ...

# 作成した全てのBlueprintをインポート
from routes.before_login import before_login_bp
from routes.registration import registration_bp
from routes.login import login_bp
from routes.home import home_bp
from routes.logout import logout_bp

app = Flask(__name__)

# --- 重要：セッションを使うために必ず設定してください ---
# このキーは他人に知られないように、実際にはもっと複雑な文字列にしてください
app.secret_key = 'your_very_secret_key_here' 

# 各Blueprintをアプリケーションに登録
app.register_blueprint(before_login_bp)
app.register_blueprint(registration_bp)
app.register_blueprint(login_bp)
app.register_blueprint(home_bp)
app.register_blueprint(logout_bp)


if __name__ == '__main__':
    # debug=True は開発中に便利なモードです
    app.run(debug=True)