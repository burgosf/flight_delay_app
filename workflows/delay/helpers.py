# import os
import logging
import datetime
# import dateutil
from dynaconf import settings
import joblib
import bisect


logger = logging.getLogger(__name__)


class DelayModelHelpers:
    def __init__(self):
        self.xgb = joblib.load('/app/workflows/delay/delay.pkl')
        self.le = joblib.load('/app/workflows/delay/le.pkl')

    def get_response(self, request):
        response = []
        origin_airport = self.get_feature_encoded('ORIGIN_AIRPORT', [request["origin"]])
        destination_airport = self.get_feature_encoded('DESTINATION_AIRPORT', [request["destination"]])
        airline = self.get_feature_encoded('AIRLINE', [request["carrier"]])
        departure_hour = request["departure_datetime"].hour
        dow = request["departure_datetime"].weekday()
        month = request["departure_datetime"].month
        day = request["departure_datetime"].day
        airtime = request['airtime']
        distance = request['distance']
        delayed = self.xgb.predict([[month, day, dow, airline, destination_airport, 
                                     origin_airport, airtime, departure_hour, distance]])[0]
        proba = self.xgb.predict_proba([[month, day, dow, airline, destination_airport, 
                                         origin_airport, airtime, departure_hour, distance]])[0][delayed]
        response = {
            "origin": request["origin"],
            "destination": request["destination"],
            "departure_datetime": request["departure_datetime"].isoformat(),
            "arrival_datetime": request["arrival_datetime"].isoformat(),
            "flight_number": request["flight_number"],
            "carrier": request["carrier"],
            "airtime": request["airtime"],
            "distance": request["distance"],
            "delayed": bool(delayed),
            "proba": round(float(proba), 4)
        }
        return response

    def get_feature_encoded(self, feature, value):
        value = ['other' if value[0] not in self.le[feature].classes_ else value[0]]
        le_classes = list(self.le[feature].classes_)
        bisect.insort_left(le_classes, 'other')
        self.le[feature].classes_ = le_classes
        result = self.le[feature].transform(value)[0]
        return result
