import json

import requests

url = "https://distance-to-coast-by-point1.p.rapidapi.com/distance-to-coast-point"

class shore_distance:
    def __init__(latitude, longitude):
        payload = {
            "lat": latitude,
            "lines": False,
            "lon": longitude
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "c494f7409cmsha8f0c89234852cbp1657d2jsndd760848d916",
            "X-RapidAPI-Host": "distance-to-coast-by-point1.p.rapidapi.com"
        }

        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.text)
        responsedata = response.json()
        print(responsedata["nearest_coastline"][0]["dist_meters"])