# --- 修正後のコード ---
from flask import Blueprint, render_template

# Blueprintの定義から template_folder を削除する
before_login_bp = Blueprint('before_login', __name__)

@before_login_bp.route('/')
def before_login():
    return render_template('before_login.html')