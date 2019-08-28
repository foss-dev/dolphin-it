from flask import Blueprint, redirect, url_for
from flask_login import logout_user, current_user

home = Blueprint('home', __name__)

@home.route('/')
def home_index():
    
    try:
        if int(current_user.get_id()) > 0:
            return redirect(url_for('system.index'))
    except:
        pass

    return redirect(url_for('auth.login'))