import requests
import pandas as pd

class LocationInformation:
    def __init__(self, userLocation):
        self.userLocation = userLocation
        self.longitude = None
        self.latitude = None
    def getLocation(self):
        key = '98a9d61a363c46bbd1f387f0b9f334ad'
        request = f'http://api.positionstack.com/v1/forward?access_key={key}&query={self.userLocation}'
        response = requests.get(request)
        data = response.json()
        self.latitude = data['data'][0]['latitude']
        self.longitude = data['data'][0]['longitude']
        return [self.latitude, self.longitude]

    def getSeaElevation(self):
        request = f'https://api.open-elevation.com/api/v1/lookup?locations={self.latitude},{self.longitude}'
        r = requests.get(request, timeout=20)
        if r.status_code == 200 | r.status_code == 201:
            self.elevation = pd.json_normalize(r.json(), 'results')['elevation'].values[0]
        else:
            self.elevation = None
        return self.elevation



