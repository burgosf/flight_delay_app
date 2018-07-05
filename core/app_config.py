import logging.config
from flask import Flask
from flask_restful import Api
from dynaconf import settings
from workflows.views import HealthCheckResource
from workflows.delay.resources import DelayResource
from .errors import (
    ValidationError,
    NotFoundError,
    ServiceUnavailableError,
    ServiceException,
    handle_exception
)

def create_app(name):
    logging.config.dictConfig(settings.LOGGING_CONFIG)
    app = Flask(name)
    app.url_map.strict_slashes = False
    app.config['PROPAGATE_EXCEPTIONS'] = True
    api = Api(app)
    api.add_resource(HealthCheckResource, '/healthcheck/')
    api.add_resource(DelayResource, '/delay/')
    app.errorhandler(ValidationError)(handle_exception)
    app.errorhandler(NotFoundError)(handle_exception)
    return app
