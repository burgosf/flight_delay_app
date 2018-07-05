from marshmallow import (
    Schema,
    fields,
    validate
)
from datetime import datetime, timezone
from marshmallow.exceptions import ValidationError


class DateValidator(object):
    def validate_future_datetime(self, date):
        now = datetime.now(timezone.utc) if date.tzinfo is not None else datetime.now()
        if date <= now:
            raise ValidationError("Please choose future datetime")

class RequestSchema(Schema):
    flight_number = fields.String(strict=True, required='flight_number is required.',
                                  validate=[validate.Length(min=3, max=7, error="3 to 7 characters")])
    departure_datetime = fields.LocalDateTime(required=True, validate=DateValidator().validate_future_datetime)
    arrival_datetime = fields.LocalDateTime(required=True, validate=DateValidator().validate_future_datetime)
    origin = fields.String(strict=True, required="origin is required",
                           validate=[validate.Length(min=3, max=3, error="3-character IATA airport code")])
    destination = fields.String(strict=True, required="destination is required",
                                validate=[validate.Length(min=3, max=3, error="3-character IATA airport code")])
    carrier = fields.String(strict=True, required="operating carrier is required",
                                      validate=[validate.Length(min=2, max=2, error="2-character IATA airline code")])
    airtime = fields.Integer(strict=True, min=1, required="airtime is required")
    distance = fields.Integer(strict=True, min=1, required="distance (in miles) is required")
