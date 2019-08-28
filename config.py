import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:

    SECRET_KEY = '4)-.W\xad\x80\x97`\x8e\xc1\xcd\x10\xd7\x11\xd6\x00\xf7M\x89\x18\xceCg'
    DOLPHINIT_VERSION = '1.0.0'
    DOLPHINITDB_VERSION = '1.0.0'
    APP_PATH = basedir


class Development(BaseConfig):

    PORT = 5000
    DEBUG = True
    TESTING = False
    ENV = 'dev'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dolphin.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(BaseConfig):

    PORT = 8080
    DEBUG = False
    TESTING = False
    ENV = 'production'

class Test(BaseConfig):

    PRESERVE_CONTEXT_ON_EXCEPTION = False
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dolphin_test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False