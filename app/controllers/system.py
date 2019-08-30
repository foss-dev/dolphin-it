import sys
import os

from flask import Blueprint, render_template, current_app
from flask_login import login_required

from ..utils import decorators

from ..models import User, db

system = Blueprint('system', __name__)

@system.route('/')
@login_required
@decorators.admin_required
def index():

    

    data = {
        "version": current_app.config.get('DOLPHINIT_VERSION'), 
        "db_version": current_app.config.get('DOLPHINITDB_VERSION'),
        "py_version": sys.version,
        "db_driver": os.getenv("DB_DRIVER"),
        "app_path": current_app.config.get('APP_PATH')
    }

    return render_template('system/system.html', data=data, page='system')


@system.route('/users')
@login_required
@decorators.admin_required
def users():

    users = User.query.all()

    data = {
        "users": users
    }

    return render_template('system/users.html', data=data, page='users')


@system.route('/projects')
@login_required
@decorators.admin_required
def projects():

    data = {}

    return render_template('system/projects.html', data=data)

@system.route('/tags')
@login_required
@decorators.admin_required
def tags():

    data = {}

    return render_template('system/tags.html', data=data)


@system.route('/roles')
@login_required
@decorators.admin_required
def roles():

    data = {}

    return render_template('system/roles.html', data=data)