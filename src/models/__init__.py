from flask_migrate import Migrate as migrate

from .base import db
from .user import User

def init_app(app):
    db.init_app(app)
    migrate(app, db)
