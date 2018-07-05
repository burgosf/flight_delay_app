import logging
from flask_restful import (
    Resource
)
from flask import (
    jsonify,
    make_response,
    request
)
from core.errors import (
    ValidationError
)
from workflows.delay.schema import (
    RequestSchema
)
from workflows.delay.helpers import (
    DelayModelHelpers
)


logger = logging.getLogger(__name__)
request_schema = RequestSchema()


class DelayResource(Resource):

    def post(self):
        req = request.get_json(force=True)
        # logger.info("request: {}".format(req))
        # Validate and deserialize input
        data, errors = request_schema.load(req)
        logger.info("data: {}".format(data))
        if errors:
            raise ValidationError(errors=errors)
        response = DelayModelHelpers().get_response(data)
        code = 200
        return make_response(jsonify({"delayed": response}), code)
