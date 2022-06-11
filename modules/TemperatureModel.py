from datetime import datetime
from meteostat import Point, Monthly
import matplotlib.pyplot as plt

class TemperatureModel:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long
        start = datetime(1970, 1, 1)
        end = datetime(2021, 12, 31)
        testLocation = Point(lat, long)
        data = Monthly(testLocation, start, end)
        data = data.fetch()
        data.to_csv('Brest.csv')
        data.plot(y=['tavg', 'tmin', 'tmax'])
        plt.show()