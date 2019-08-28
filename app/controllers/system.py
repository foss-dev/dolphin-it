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

    # http://localhost/mantis/manage_user_page.php

    users = User.query.all()

    data = {
        "version": current_app.config.get('DOLPHINIT_VERSION'), 
        "db_version": current_app.config.get('DOLPHINITDB_VERSION'),
        "py_version": sys.version,
        "db_driver": os.getenv("DB_DRIVER"),
        "app_path": current_app.config.get('APP_PATH'),
        "users": users
    }

    return render_template('system/system.html', data=data)