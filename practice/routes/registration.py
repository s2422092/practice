from flask import Blueprint, render_template, request, redirect, url_for, flash
import sqlite3
from werkzeug.security import generate_password_hash
import os

# Blueprint の定義
registration_bp = Blueprint('registration', __name__)

# 登録ページルート
@registration_bp.route('/registration', methods=['GET', 'POST'])
def registration():
    return render_template('registration.html')