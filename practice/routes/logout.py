from flask import session, redirect, url_for, Blueprint, flash

# Blueprint名は 'logout' の方が分かりやすいかもしれません
logout_bp = Blueprint('logout', __name__)

@logout_bp.route('/logout')
def logout():
    # セッションからユーザー情報を削除
    session.pop('user_id', None)
    session.pop('username', None)
    
    # またはセッション全体をクリア
    # session.clear()

    flash('ログアウトしました', 'info')
    # ログアウト後は、ログイン前のトップページにリダイレクト
    return redirect(url_for('before_login.before_login'))