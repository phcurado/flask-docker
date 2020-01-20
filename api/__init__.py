from flask import Flask
from flask_migrate import upgrade
from api.config import DevelopmentConfig
from sqlalchemy_utils import database_exists, create_database

def create_app(config_class=DevelopmentConfig):
    setup_logs()
    app = Flask(__name__)

    app.config.from_object(config_class)

    setup_database(app, config_class.SQLALCHEMY_DATABASE_URI)
    
    setup_routes(app)

    return app

def setup_database(app, db_uri):
    # create database if not exist
    if not database_exists(db_uri):
        create_database(db_uri)

    # Import database instance with SQLAlchemy
    from .app import database
    database.init_app(app)

    # Run Migrations
    with app.app_context():
        upgrade()
    
def setup_routes(app):
    from .web import controllers
    controllers.init_app(app)

def setup_logs():
    from logging.config import dictConfig

    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'WARN',
            'handlers': ['wsgi']
        }
    })
