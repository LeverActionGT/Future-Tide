#Rishit
import re

import requests
import pandas as pd
import modules.token_reader
from meteostat import Point, Monthly
from datetime import datetime

class Geocoding:
    def __init__(self, user_location): #user_location is string address
        #put input into class attribute
        geo = re.sub(r'\W', ' ', user_location)
        self.user_location = "%20".join(geo.split())
        self.latitude = None
        self.longitude = None
        #rint(self.user_location)
        #positionstack geocoding API call
        positionstack_token = modules.token_reader.tokens()['positionstack']
        #print(positionstack_token)
        request = f'http://api.positionstack.com/v1/forward?access_key={positionstack_token}&query={self.user_location}'
        response = requests.get(request)
        if response.status_code == 200 or response.status_code == 201:
            data = response.json()
            #print(data)
            self.latitude = data['data'][0]['latitude']
            self.longitude = data['data'][0]['longitude']
            self.label = data['data'][0]['label']
        elif response.status_code == 404: 
            raise Exception('404, PositionStack API not accessible')

        #open-elevation elev API call
        request = f'https://api.open-elevation.com/api/v1/lookup?locations={self.latitude},{self.longitude}'
        r = requests.get(request, timeout=20)
        if r.status_code == 200 or r.status_code == 201:
            self.elevation = pd.json_normalize(r.json(), 'results')['elevation'].values[0]
        else:
            self.elevation = None

        start = datetime(2017, 1, 1)
        end = datetime(2019, 12, 31)
        testLocation = Point(48.404244, -4.484974)
        data = Monthly(testLocation, start, end)
        data = data.fetch()
        data = data['tavg']
        add = 0
        nan_count = 0
        for i in range(0, len(data)):
            if data[i] != np.nan:
                add += i
        else:
            nan_count += 1
        if nan_count == len(data):
            avg_temp = 15
        else:
            avg_temp = add/len(data)
        self.avg_temp = avg_temp
