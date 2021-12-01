import os
import tempfile

import pytest
from ratesapp import create_app


@pytest.fixture
def app():

    app = create_app({
        'TESTING': True,
    })

    app.config.from_object('ratesapp.config.Config')

    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
