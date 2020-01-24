import pytest
from api import create_ap
from api.config import TestingConfig
from api.app.database.instance import db

from sqlalchemy_utils import database_exists, drop_database

@pytest.fixture(scope='session', autouse=True)
def client():
    app = create_app(TestingConfig)

    with app.test_client() as client:
        #  with app.app_context():
        #     some function with need context before tests
        yield client
    # after the tests we drop the database created for this purpose
    if database_exists(TestingConfig.SQLALCHEMY_DATABASE_URI):
        drop_database(TestingConfig.SQLALCHEMY_DATABASE_URI)

    