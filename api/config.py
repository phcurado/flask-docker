from os import environ

# SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
# SQLALCHEMY_TRACK_MODIFICATIONS = False


class Config(object):
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False

class DevelopmentConfig(Config):
    TESTING = False

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_TEST_URL')
    TESTING = True