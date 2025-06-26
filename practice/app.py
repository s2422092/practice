from flask import Flask
from routes.before_login.before_login import before_login_bp
from routes.after_login.after_login import after_login_bp

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Blueprintの登録
app.register_blueprint(before_login_bp)
app.register_blueprint(after_login_bp)

app.static_folder = 'staicts'
app.template_folder = 'template'

if __name__ == '__main__':
    app.run(debug=True)
