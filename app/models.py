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

class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    create_project = db.Column(db.Boolean(), default=False)
    edit_project = db.Column(db.Boolean(), default=False)
    delete_project = db.Column(db.Boolean(), default=False)
    project_status = db.Column(db.Boolean(), default=False)
    add_project_tag = db.Column(db.Boolean(), default=False)
    add_project_category = db.Column(db.Boolean(), default=False)
    edit_project_description = db.Column(db.Boolean(), default=False)
    create_issue = db.Column(db.Boolean(), default=False)
    edit_issue = db.Column(db.Boolean(), default=False)
    delete_issue = db.Column(db.Boolean(), default=False)
    issue_status = db.Column(db.Boolean(), default=False)
    assign_issue = db.Column(db.Boolean(), default=False)
    move_issue = db.Column(db.Boolean(), default=False)
    add_issue_comment = db.Column(db.Boolean(), default=False)
    edit_issue_comment = db.Column(db.Boolean(), default=False)
    delete_issue_comment = db.Column(db.Boolean(), default=False)
    edit_issue_description = db.Column(db.Boolean(), default=False)
    add_issue_user = db.Column(db.Boolean(), default=False)
    edit_issue_user = db.Column(db.Boolean(), default=False)
    delete_issue_user = db.Column(db.Boolean(), default=False)
    add_attachment_issue = db.Column(db.Boolean(), default=False)