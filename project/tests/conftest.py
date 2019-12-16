import pytest
from project import app, db

@pytest.fixture(scope='module')
def test_app():
    # setup
    app.config.from_object('project.config.TestingConfig')
    with app.app_context():
        # testing
        yield app

@pytest.fixture(scope='module')
def test_database():
    # setup
    db.create_all()
    # testing
    yield db
    # teardown
    db.session.remove()
    db.drop_all()