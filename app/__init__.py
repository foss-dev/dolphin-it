import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__))
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

# https://scotch.io/tutorials/authentication-and-authorization-with-flask-login

# wtf form => https://flask-wtf.readthedocs.io/en/stable/
# csrf token => https://flask-wtf.readthedocs.io/en/v0.12/csrf.html

config = {
    "development": "config.Development",
    "production": "config.Production",
    "test": "config.Test"
}

csrf = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()

def create_app(cfg: str = ''):

    app = Flask(__name__)

    env = (os.getenv('ENV') or os.getenv('FLASK_ENV')) or 'development'

    if cfg:
        env = cfg

    app.config.from_object(config.get(env))

    csrf.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    app.app_context().push()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):

        return User.query.get(int(user_id))

    from .controllers.home import home
    from .controllers.auth import auth
    from .controllers.system import system

    app.register_blueprint(home)
    app.register_blueprint(auth)
    app.register_blueprint(system, url_prefix='/system')

    return app