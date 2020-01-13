from flask_migrate import Migrate, MigrateCommand

from .base import db
from .user import User

def init_app(app):
    db.init_app(app)
    Migrate(app, db)
