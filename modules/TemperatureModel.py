from datetime import datetime
from meteostat import Point, Monthly
import matplotlib.pyplot as plt

class TemperatureModel:
    def __init__(self, lat, long, ele):
        self.lat = lat
        self.long = long
        self.ele = ele
        request = f''
        start = datetime(1970, 1, 1)
        end = datetime(2021, 12, 31)
        testLocation = Point(lat, long, ele)
        data = Monthly(testLocation, start, end)
        data = data.fetch()
        data.to_csv('Australia.csv')
        data.plot(y=['tavg', 'tmin', 'tmax'])
        plt.show()

tm = TemperatureModel(-33.854667, 151.225778, 3.3)
