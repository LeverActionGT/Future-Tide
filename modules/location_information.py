#Rishit

import requests
import pandas as pd
import config_reader

class LocationInformation:
    def __init__(self, userLocation):
        self.userLocation = userLocation
        self.longitude = None
        self.latitude = None

    def getLocation(self):
        positionstack_token = config_reader.configs()['positionstack']
        request = f'http://api.positionstack.com/v1/forward?access_key={positionstack_token}&query={self.userLocation}'
        response = requests.get(request)
        if response.status_code == 200 | response.status_code == 201:
            data = response.json()
            self.latitude = data['data'][0]['latitude']
            self.longitude = data['data'][0]['longitude']
            return [self.latitude, self.longitude]
        elif response.status_code == 404:
            return("error")

    def getSeaElevation(self):
        request = f'https://api.open-elevation.com/api/v1/lookup?locations={self.latitude},{self.longitude}'
        r = requests.get(request, timeout=20)
        if r.status_code == 200 | r.status_code == 201:
            self.elevation = pd.json_normalize(r.json(), 'results')['elevation'].values[0]
        else:
            self.elevation = None
        return self.elevation