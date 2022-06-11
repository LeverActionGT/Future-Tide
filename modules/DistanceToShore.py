import requests

url = "https://distance-to-coast-by-point1.p.rapidapi.com/distance-to-coast-point"

class shore_distance:
    def __init__(latitude, longitude):
        payload = {
            "lat": 44.501226,
            "lines": False,
            "lon": -88.062187
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "4593d5ade1msh94b625aa3071c91p1df6f0jsnf2190bc028a6",
            "X-RapidAPI-Host": "distance-to-coast-by-point1.p.rapidapi.com"
        }

        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.text)