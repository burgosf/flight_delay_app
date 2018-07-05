from .base import BaseTest
import datetime
from workflows.delay.schema import RequestSchema
from workflows.delay.helpers import DelayModelHelpers



class Request(BaseTest):

    def setUp(self):
        self.requestschema = RequestSchema()
        self.request = {
            "flight_number": "UA1268",
            "departure_datetime": "2018-08-02T16:45:00",
            "arrival_datetime": "2018-08-02T19:05:00",
            "origin": "SFO",
            "destination": "DEN",
            "carrier": "UA",
            "airtime": 80,
            "distance": 650
        }

    def test_bad_datetime(self):
        bad_datetime = ["2018-12-aa", "2018-12-15T16:45,00", "2017-12-15T16:45:00Z"]
        bad_datetime_error = [{'departure_datetime': ['Not a valid datetime.']},
                              {'departure_datetime': ['Not a valid datetime.']},
                              {'departure_datetime': ['Please choose future datetime']}]
        for idx, item in enumerate(bad_datetime):
            self.request['departure_datetime'] = item
            errors = self.requestschema.load(self.request)[1]
            # errors = self.flightschema.load(self.flight)
            # print("errors: {}".format(errors))
            self.assertEqual(errors, bad_datetime_error[idx])

    def test_bad_airport(self):
        bad_airport = ["AAAA", "BB", 123]
        bad_airport_error = [{'origin': ['3-character IATA airport code']}, {'origin': ['3-character IATA airport code']},
                             {'origin': ['Not a valid string.']}]
        for idx, item in enumerate(bad_airport):
            self.request['origin'] = item
            errors = self.requestschema.load(self.request)[1]
            self.assertEqual(errors, bad_airport_error[idx])

    def test_flight_number(self):
        bad_flight_number = [123, "EK", "flight_number"]
        bad_flight_number_error = [{'flight_number': ['Not a valid string.']},
                                   {'flight_number': ['3 to 7 characters']},
                                   {'flight_number': ['3 to 7 characters']}]
        for idx, item in enumerate(bad_flight_number):
            self.request['flight_number'] = item
            errors = self.requestschema.load(self.request)[1]
            self.assertEqual(errors, bad_flight_number_error[idx])


class Delay(BaseTest):

    def setUp(self):
        self.delay = DelayModelHelpers()
        self.request = {
            "flight_number": "UA1268",
            "departure_datetime": datetime.datetime.utcnow() + datetime.timedelta(days=34),
            "arrival_datetime": datetime.datetime.utcnow() + datetime.timedelta(days=34) + datetime.timedelta(minutes=120),
            "origin": "SFO",
            "destination": "DEN",
            "carrier": "UA",
            "airtime": 80,
            "distance": 650
        }

    def test_delay(self):
        response = self.delay.get_response(self.request)
        self.assertFalse(response["delayed"])

    def test_proba(self):
        response = self.delay.get_response(self.request)
        self.assertTrue(response["proba"] > 0.0)
        self.assertTrue(response["proba"] < 1.0)
