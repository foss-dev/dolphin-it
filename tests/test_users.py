import unittest
import random
import string

from werkzeug.security import generate_password_hash, check_password_hash

from app import create_app, db
from app.models import User

# https://kapeli.com/cheat_sheets/Python_unittest_Assertions.docset/Contents/Resources/Documents/index
# https://awholestack.com/posts/basic-flask-app/


class UsersTestCase(unittest.TestCase):

    """
    Test users table create
    """

    def setUp(self):
        self.app = create_app('test')
        
        db.init_app(self.app)
        db.create_all(app=self.app)

        self.client = self.app.test_client()
        
    def test_add_user(self):

        letters = string.ascii_lowercase
        random_letter = ''.join(random.choice(letters) for i in range(10))
        random_letter_end = ''.join(random.choice(letters) for i in range(10))

        name = "Ali GOREN"
        email = f"{random_letter}@{random_letter_end}"
        username = random_letter
        password = random_letter

        new_user = False

        user = User.query.filter((User.email==email) | (User.username==username)).first()

        if not user:
            new_user = User(name=name, email=email, username=username, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()

        self.assertTrue(new_user, 'The user couldn\'t be added')
        
    def test_get_users(self):
        users = User.query.all()

        self.assertTrue(len(users) > 0, 'There are no users')