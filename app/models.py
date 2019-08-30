from flask_login import UserMixin

from app import create_app, db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(300))
    is_admin = db.Column(db.Boolean(), default=False)
    access_level = db.Column(db.Integer, default=10)
    is_active = db.Column(db.Boolean(), default=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now())


class AccessLevel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level_name = db.Column(db.String(150), unique=True)