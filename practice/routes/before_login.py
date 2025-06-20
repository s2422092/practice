from flask import Blueprint, render_template, request, redirect, url_for, flash
import sqlite3
from werkzeug.security import generate_password_hash
import os

# Blueprint の定義
before_login_bp = Blueprint('before_login', __name__)

# 登録ページルート
@before_login_bp.route('/before_login', methods=['GET', 'POST'])
def before_login():
    
    return render_template('')