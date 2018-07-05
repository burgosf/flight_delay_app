import pytest
from flask import Flask
from core.app_config import create_app


@pytest.fixture(scope='session')
def app(request) -> Flask:
    example_app = create_app('test')
    example_app.testing = True
    ctx = example_app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return example_app
