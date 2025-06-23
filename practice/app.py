from flask import Flask
from routes import (
    before_login_bp
)

app = Flask(__name__, template_folder='templates', static_folder='static')

# 🔒 セッションなどに必要なシークレットキーを設定
app.secret_key = 'your_secret_key_here'  # ← 好きなランダムな文字列でOK


# ルートの登録
app.register_blueprint(before_login_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # デバッグモードでポート5000で実行