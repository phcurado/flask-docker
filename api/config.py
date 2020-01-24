from os import environ

class Config(object):
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False

class DevelopmentConfig(Config):
    TESTING = False

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_TEST_URL')
    TESTING = True

def set_config_class():
    env = environ.get('FLASK_ENV')
    if env == 'development':
        return DevelopmentConfig
    elif env == 'production':
        return Config
