import json

import requests

url = "https://distance-to-coast-by-point1.p.rapidapi.com/distance-to-coast-point"

class shore_distance:
    def __init__(self, latitude, longitude):
        payload = {
            "lat": latitude,
            "lines": False,
            "lon": longitude
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": '172ba95d39mshd35ec8407693336p15ca25jsnfe5ce8149ffc',
            "X-RapidAPI-Host": "distance-to-coast-by-point1.p.rapidapi.com"
        }

        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.text)
        responsedata = response.json()
        print(responsedata["nearest_coastline"][0]["dist_meters"])
        self.output = responsedata["nearest_coastline"][0]["dist_meters"]