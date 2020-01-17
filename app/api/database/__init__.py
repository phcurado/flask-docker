from flask_migrate import Migrate
from .instance import db
from app.api.models import *

def init_app(app):
    db.init_app(app)
    Migrate(app, db)
