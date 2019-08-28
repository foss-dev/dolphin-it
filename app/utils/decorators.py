from functools import wraps

from flask import flash, render_template
from flask_login import current_user

#https://pythonise.com/feed/flask/custom-flask-decorators

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin:
            flash("You do not have permission to view that page", "danger")
            return render_template('error/403.html')
        
        return f(*args, **kwargs)
    
    return decorated_function