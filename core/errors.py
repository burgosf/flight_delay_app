from flask import jsonify


class ServiceException(Exception):
    status_code = 500
    message = "Service Unavailable!"

    def __init__(self, message=None, errors=[]):
        super().__init__()
        self.payload = {}
        if message:
            self.message = message
        self.payload['errors'] = errors

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


class ValidationError(ServiceException):
    status_code = 400
    message = "Validation Error!"


class NotFoundError(ServiceException):
    status_code = 404
    message = "Not Found!"


class ServiceUnavailableError(ServiceException):
    status_code = 503
    message = "Service Unavailable!"


def handle_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
