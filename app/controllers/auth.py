from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

from ..models import User
from .. import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    try:
        if int(current_user.get_id()) > 0:
            return redirect(url_for('system.index'))
    except:
        pass
    
    if request.method == 'GET':
        return render_template('auth/login.html')
    else:

        username = request.form.get('username')
        password = request.form.get('password')
        remember = request.form.get('remember')
        
        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.', 'info')
            return redirect(url_for('auth.login'))

        login_user(user, remember=remember)
        return redirect(url_for('system.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():

    try:
        if int(current_user.get_id()) > 0:
            return redirect(url_for('system.index'))
    except:
        pass

    if request.method == 'GET':
        return render_template('auth/register.html')
    else:
        name = request.form.get('name')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter((User.email==email) | (User.username==username)).first()

        if user:
            flash('User already exists', 'danger')
            return redirect(url_for('auth.register'))
        
        new_user = User(name=name, email=email, username=username, password=generate_password_hash(password, method='sha256'))

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))

@auth.route('/profile')
@login_required
def profile():
    user = current_user
    return render_template('auth/profile.html', user=user)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))